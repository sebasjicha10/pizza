from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User

class Dish(models.Model):
    product = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.product} {self.name} {self.price}"

class Extra(models.Model):
    product = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        if self.product == "Topping":
            return f"{self.product}: {self.name}"
        return f"{self.product}: {self.name} {self.price}"

class Item(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    extras = models.ManyToManyField(Extra, blank=True)
    price = models.FloatField()

    def __str__(self):
        return f"{self.dish} {self.extras.all()} {self.price}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return f"{self.id} {self.user}"

class Order(models.Model):
    ORDER_STATUS = (
        ("PN", "Pending"),
        ("CN", "Canceled"),
        ("DL", "Delivered")
    )
    items = models.ManyToManyField(Item, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(choices=ORDER_STATUS, max_length=3, default="PN")

    def __str__(self):
        return f"Status: {self.status}, ID: {self.id}, Time:{self.created.hour}:{self.created.minute}, User: {self.user}, Total: {self.total}"

