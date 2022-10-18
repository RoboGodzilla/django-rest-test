from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=7, decimal_places=2)

  def __str__(self):
      return self.name

class Customer(models.Model):
  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)

  def __str__(self):
      return self.name