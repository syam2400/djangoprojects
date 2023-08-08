from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='shop/category', null=True, blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='shop/products', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
