from sapapp.models import Sapproductionorder,Sapproduct
from rest_framework import serializers

class SapProductionOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sapproductionorder
        fields = "__all__"
class SapProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sapproduct
        fields = "__all__"