from sapapp.models import Sapproductionorder,Sapproduct
from rest_framework import serializers

class SapProductionOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sapproductionorder
        fields = "__all__"
        # fields = ["process_order_number","created_by","batch_number","gln_number","regulation"," packaging_Version",
        #           "production_date","requested","produced","status","gtin_number","imn","expiration_date","serialnoprovider"]
class SapProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sapproduct
        fields = "__all__"