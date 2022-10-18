from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from django.shortcuts import get_object_or_404

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [permissions.IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  permission_classes = [permissions.IsAuthenticated]

  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

  def update(self, request, pk = None):
        try:
            obj = get_object_or_404(Customer, pk = pk)
            request.data['updated_by'] = request.user.pk
            serializer = CustomerSerializer(obj, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            ################## START ERROR #################################
            # exc = sys.exc_info()
            # directorio = os.path.split(os.path.dirname(__file__))[1] + '/' + os.path.split(exc[2].tb_frame.f_code.co_filename)[1]
            # error_log(e, exc[0], exc[2].tb_lineno, directorio, request.user.username)
            # data = {'mensaje_error': str(e)}
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [permissions.IsAuthenticated]