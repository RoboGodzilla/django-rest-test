from django.db import models
from entidades.models import Product, Customer

# Create your models here.
class Warehouse(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  max_racks_qty = models.IntegerField()
  max_total_weight = models.IntegerField()

  def __str__(self):
      return self.name

class Rack(models.Model):
  name = models.CharField(max_length=100)
  warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)

  def __str__(self):
      return self.name

class Level(models.Model):
  name = models.CharField(max_length=100)
  rack = models.ForeignKey(Rack, on_delete=models.PROTECT)

  def __str__(self):
      return self.name

class Space(models.Model):
  name = models.CharField(max_length=100)
  level = models.ForeignKey(Level, on_delete=models.PROTECT)

  def __str__(self):
      return self.name

class Section(models.Model):
  name = models.CharField(max_length=100)
  space = models.ForeignKey(Space, on_delete=models.PROTECT)
  max_weight = models.IntegerField()

  def __str__(self):
      return self.name

class Pallet(models.Model):
  id = models.AutoField(primary_key=True)
  section = models.ForeignKey(Section, on_delete=models.PROTECT)
  code = models.IntegerField()
  is_empty = models.BooleanField(default=False)

  def __str__(self):
      return self.code

class PalletProduct(models.Model):
  pallet = models.ForeignKey(Pallet, on_delete=models.PROTECT)
  product = models.ForeignKey(Product, on_delete=models.PROTECT)
  quantity = models.IntegerField()

  def __str__(self):
      return self.pallet.code + " - " + self.product.name

class Inventory(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
  product = models.ForeignKey(Product, on_delete=models.PROTECT)
  warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
  quantity = models.IntegerField()

  def __str__(self):
      return self.product.name + " - " + self.quantity + " - " + self.customer.name