from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.forms import TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Dish, Extra, Item, Cart, Order

import smtplib


# Registration Form
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder':'Username', "class": "register_input", "class": "register_input"}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', "class": "register_input"}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name', "class": "register_input"}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'placeholder':'Email', "class": "register_input"}))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password', "class": "register_input"}))
    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation', "class": "register_input"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

  
# Views
def index(request):
    """ Index page """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = len(cart.items.all())
    except:
        cart_items = 0

    return render(request, "orders/index.html", {
        "menu": Dish.objects.all(),
        "extra": Extra.objects.all(),
        "cart_items": cart_items
    })


def login_view(request):
    """ Log in Page """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {
                "message": "Invalid credentials."
            })
        
    return render(request, "orders/login.html")


def logout_view(request):
    """ Log out """
    logout(request)
    return render(request, "orders/login.html", {
        "message": "Logged out."
    })


def register_view(request):
    """ Registration Page """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "orders/register.html", {"form": form})


def add_item(request):
    """ Add Item to Cart """

    if request.method == "GET":
        return HttpResponseRedirect(reverse("index"))
    
    # Variable definition
    try:
        dish = Dish.objects.get(pk=(request.POST["dish"]))
    except:
        return HttpResponseRedirect(reverse("index"))

    extra = request.POST.getlist('extra')

    # No toppings Pizza validator
    if (dish.pk == 1 or dish.pk == 2 or dish.pk == 11 or dish.pk == 12) and len(extra) != 0:
        return HttpResponseRedirect(reverse("index"))

    # 1 topping Pizza validator
    if (dish.pk == 3 or dish.pk == 4 or dish.pk == 13 or dish.pk == 14) and len(extra) != 1:
        return HttpResponseRedirect(reverse("index"))

    # 2 toppings Pizza validator
    if (dish.pk == 5 or dish.pk == 6 or dish.pk == 15 or dish.pk == 16) and len(extra) != 2:
        return HttpResponseRedirect(reverse("index"))

    # 3 toppings Pizza validator
    if (dish.pk == 7 or dish.pk == 8 or dish.pk == 17 or dish.pk == 18) and len(extra) != 3:
        return HttpResponseRedirect(reverse("index"))

    # Special Pizza Pizza validator
    if (dish.pk == 9 or dish.pk == 10 or dish.pk == 19 or dish.pk == 20) and len(extra) != 5:
        return HttpResponseRedirect(reverse("index"))
        
    # Item variables
    extras = []
    price = dish.price

    for item in extra:
        new_extra = Extra.objects.get(pk=(item))
        extras.append(new_extra)
        price += new_extra.price

    new_item = Item(dish=dish, price=price)
    new_item.save()
    for item in extras:
        new_item.extras.add(item)

    # Cart Handling
    try:
        cart = Cart.objects.get(user=request.user)
    except:
        cart = Cart(user=request.user)
        cart.save()
    cart.items.add(new_item)
    cart.save()

    return HttpResponseRedirect(reverse("index"))
    
        
def shopping_cart_view(request):
    """ Shopping Cart View """
    try:
        cart = Cart.objects.get(user=request.user)
    except:
        return HttpResponseRedirect(reverse("index"))
    items = cart.items.all()
    total = 0
    for item in items:
        total += item.price
    return render(request, "orders/shopping_cart.html", {
        "cart": items,
        "total": total,
    })


def order(request):
    """ Place order """
    # Variables
    cart = Cart.objects.get(user=request.user)
    items = cart.items.all()
    total = request.POST["total"]
    
    new_order = Order(total=total, user=request.user)
    new_order.save()

    for item in items:
        new_item = Item.objects.get(pk=item.id)
        new_order.items.add(new_item)

    new_order.save()
    cart.delete()

    # Email confirmation 
    user_email = request.user.email
    content = f"Dear Customer, your order({new_order.pk}) has been successfully processed.\nOrders details:\n    Number of items: {len(items)}\n    Total: {total}\n\n\nPinocchio's Pizza & Subs"
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("pinocchios.pizzas.subs@gmail.com", "Gmailaccountforproject3")
    mail.sendmail("pinocchios.pizzas.subs@gmail.com", user_email, content)
    mail.close()

    return HttpResponseRedirect(reverse("index"))


def clear_cart(request):
    """ Clear Shopping Cart """
    cart = Cart.objects.get(user=request.user)
    cart.delete()
    return HttpResponseRedirect(reverse("index"))
