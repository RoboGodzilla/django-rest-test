from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404

# Create your views here.

class WarehouseViewSet(viewsets.ModelViewSet):
  queryset = Warehouse.objects.all()
  serializer_class = WarehouseSerializer
  permission_classes = [permissions.IsAuthenticated]

class RackViewSet(viewsets.ModelViewSet):
  queryset = Rack.objects.all()
  serializer_class = RackSerializer
  permission_classes = [permissions.IsAuthenticated]

class LevelViewSet(viewsets.ModelViewSet):
  queryset = Level.objects.all()
  serializer_class = LevelSerializer
  permission_classes = [permissions.IsAuthenticated]

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SpaceViewSet(viewsets.ModelViewSet):
  queryset = Space.objects.all()
  serializer_class = SpaceSerializer
  permission_classes = [permissions.IsAuthenticated]

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SectionViewSet(viewsets.ModelViewSet):
  queryset = Section.objects.all()
  serializer_class = SectionSerializer
  permission_classes = [permissions.IsAuthenticated]

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PalletViewSet(viewsets.ModelViewSet): 
  queryset = Pallet.objects.all()
  serializer_class = PalletSerializer
  permission_classes = [permissions.IsAuthenticated]

class PalletProductViewSet(viewsets.ModelViewSet):
  queryset = PalletProduct.objects.all()
  serializer_class = PalletProductSerializer
  permission_classes = [permissions.IsAuthenticated]

class InventoryViewSet(viewsets.ModelViewSet):
  queryset = Inventory.objects.all()
  serializer_class = InventorySerializer
  permission_classes = [permissions.IsAuthenticated]