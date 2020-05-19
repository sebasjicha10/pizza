from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("add_item", views.add_item, name="add_item"),
    path("cart", views.shopping_cart_view, name="cart"),
    path("order", views.order, name="order"),
    path("clear_cart", views.clear_cart, name="clear_cart")
]
