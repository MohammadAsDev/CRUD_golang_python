from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(name="product_name" , max_length=100)
    description = models.CharField(name="product_description" , max_length=200)