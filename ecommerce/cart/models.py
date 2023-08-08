from django.db import models
from shop.models import Products
from django.contrib.auth.models import User


class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    data_added = models.DateField(auto_now_add=True)

    def subtotal(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=30)
    order_status = models.CharField(max_length=30, default='pending')
    delivery_status = models.CharField(max_length=30, default='pending')
    no_of_items = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def subtotal(self):
        return self.no_of_items * self.products.price


class Account(models.Model):
    acc_number = models.CharField(max_length=30)
    acc_type = models.CharField(max_length=30)
    amount = models.IntegerField()

    def __str__(self):
        return self.acc_number
