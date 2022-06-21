from distutils.command.upload import upload
from operator import mod
from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length = 100)
    district = models.CharField(max_length = 150)
    address = models.CharField(max_length = 50)
    number = models.CharField(max_length = 20)
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 15)
    createdAt = models.DateField(default = date.today)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to='product_photo', null=True, blank=True)
    name = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50)
    quantity = models.CharField(max_length = 25)
    price = models.FloatField()
    description = models.CharField(max_length = 150)
    createdAt = models.DateField(default = date.today)
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name
