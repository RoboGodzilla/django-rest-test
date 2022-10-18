from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404

# Create your views here.
class RequestViewSet(viewsets.ModelViewSet):
  queryset = Request.objects.all()
  serializer_class = RequestSerializer
  permission_classes = [permissions.IsAuthenticated]

class RequestProductViewSet(viewsets.ModelViewSet):
  queryset = RequestProduct.objects.all()
  serializer_class = RequestProductSerializer
  permission_classes = [permissions.IsAuthenticated]

class InputViewSet(viewsets.ModelViewSet):
  queryset = InputWarehouse.objects.all()
  serializer_class = InputSerializer
  permission_classes = [permissions.IsAuthenticated]

class InputPalletViewSet(viewsets.ModelViewSet):
  queryset = InputPalletProduct.objects.all()
  serializer_class = InputPalletSerializer
  permission_classes = [permissions.IsAuthenticated]

class OutputViewSet(viewsets.ModelViewSet):
  queryset = OutputWarehouse.objects.all()
  serializer_class = OutputSerializer
  permission_classes = [permissions.IsAuthenticated]

class OutputPalletViewSet(viewsets.ModelViewSet):
  queryset = OutputPalletProduct.objects.all()
  serializer_class = OutputPalletSerializer
  permission_classes = [permissions.IsAuthenticated]