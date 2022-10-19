from django.db import models
from entidades.models import Product, Customer
from bodegas.models import Warehouse, PalletProduct
import datetime

# Create your models here.
class Request(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
  motive = models.CharField(max_length=200)
  movement = models.IntegerField()
  approved = models.BooleanField(default=False)
  canceled = models.BooleanField(default=False)
  products = models.ManyToManyField(Product, through='RequestProduct')

  def __str__(self):
    return self.customer.name + " - " + self.motive

  def save(self, force_insert=False, force_update=False, *args, **kwargs):
    # solo modelos existentes
    if self.pk:
        # chequear si el pedido fue aprobado
        _original_request = Request.objects.get(id=self.pk)
        if _original_request.price != self.price:
            # crear ingreso de bodega y guardar update
            InputWarehouse.objects.create(request_id=self.id, warehouse_id=1)
            super(Request, self).save(force_insert, force_update, *args, **kwargs)
    super(Request, self).save(force_insert, force_update, *args, **kwargs)

class RequestProduct(models.Model):
  request = models.ForeignKey(Request, on_delete=models.PROTECT)
  product = models.ForeignKey(Product, on_delete=models.PROTECT)
  quantity = models.IntegerField()

  def __str__(self):
      return self.request + " - " + self.product.name + " - " + self.quantity

class InputWarehouse(models.Model):
  request = models.ForeignKey(Request, on_delete=models.PROTECT)
  warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
  date = models.DateField(default=datetime.date.today)
  number = models.IntegerField()
  comments = models.CharField(max_length=200, blank=True, null=True)

  def __str__(self):
    return self.request.customer.name + " - " + self.request.product.name + " - " + self.date

  def save(self, force_insert=False, force_update=False, *args, **kwargs):
    # solo modelos existentes
    if self.pk:
      # chequear si el pedido fue aprobado
      _original_request = Request.objects.get(id=self.pk)
      if _original_request.price != self.price:
          # crear ingreso de bodega y guardar update
          InputWarehouse.objects.create(request_id=self.id, warehouse_id=1)
          super(Request, self).save(force_insert, force_update, *args, **kwargs)
    super(Request, self).save(force_insert, force_update, *args, **kwargs)


class InputPalletProduct(models.Model):
  input = models.ForeignKey(InputWarehouse, on_delete=models.PROTECT)
  pallet_product = models.ForeignKey(PalletProduct, on_delete=models.PROTECT)
  quantity = models.IntegerField()

  def __str__(self):
    return self.pallet_product.product.name + " - " + self.quantity + " - " + self.output.date
    
class OutputWarehouse(models.Model):
  request = models.ForeignKey(Request, on_delete=models.PROTECT)
  warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
  date = models.DateField(default=datetime.date.today)
  number = models.IntegerField()
  comments = models.CharField(max_length=200, blank=True, null=True)

  def __str__(self):
    return self.request.customer.name + " - " + self.request.product.name + " - " + self.date

class OutputPalletProduct(models.Model):
  output = models.ForeignKey(OutputWarehouse, on_delete=models.PROTECT)
  pallet_product = models.ForeignKey(PalletProduct, on_delete=models.PROTECT)
  quantity = models.IntegerField()

  def __str__(self):
    return self.pallet_product.product.name + " - " + self.quantity + " - " + self.output.date