# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=500)
    link = models.URLField(max_length=2000)
    rating = models.DecimalField(max_digits=3,decimal_places=2)
    features = models.CharField(max_length=1000,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.FilePathField(max_length=255)
    category = models.CharField(max_length=255,default='')

    def insert(self,products,product_category):
        Product.objects.bulk_create([
            Product(
                name = item['name'],
                link = item['link'],
                rating = item['rating'],
                features = item['features'],
                price = item['price'],
                image = item['image'],
                category = product_category
            ) for item in products
        ])