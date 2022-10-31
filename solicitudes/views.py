from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *

# Create your views here.
class RequestViewSet(viewsets.ModelViewSet):
  queryset = Request.objects.all()
  serializer_class = RequestSerializer
  permission_classes = [permissions.IsAuthenticated]

  @action(methods=['get'], detail=False, url_path='active', url_name='active')
  def unapproved_requests(self, request):
    try:
        unarequest = Request.objects.filter(approved = False, canceled = False)
        customer_list = dict()
        for request in unarequest:
            product_list = list()
            product_names = list()
            for product in request.products.all():
                product_list.append(product.id)
                product_names.append(product.name)
            customer_list[request.id] = { 'customer': request.customer.name, 'motive': request.motive, 'products': product_list, 'product_names': product_names }
        return Response(customer_list, status=status.HTTP_200_OK)
    except Exception as e:
        ################## START ERROR #################################
        data = {'mensaje_error': str(e)}
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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