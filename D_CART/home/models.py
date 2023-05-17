from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='productImage')
    price=models.CharField(max_length=255)
    raring=models.CharField(max_length=10)
    brand=models.CharField(max_length=200)
    stock=models.CharField(max_length=200)
    discription=models.CharField(max_length=300)
    color=models.CharField(max_length=200)