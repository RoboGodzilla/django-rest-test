from rest_framework import serializers

from .models import *

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class RequestProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestProduct
        fields = '__all__'

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputWarehouse
        fields = '__all__'

class InputPalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputPalletProduct
        fields = '__all__'

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutputWarehouse
        fields = '__all__'

class OutputPalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutputPalletProduct
        fields = '__all__'