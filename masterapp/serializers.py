from masterapp.models import Company,Customers,BarCodeType,SnProvider, Stock,Locations,ShipPO,ProductionOrder,Product
from rest_framework import serializers
class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Company
        fields = ['id','company_name','created_by']
class CustomersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Customers
        fields =['id','name','created_by','company_prefix','company_gln','address','zip']
        # fields="__all__"
class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Locations
        fields = ['id','customer_id','name','created_by','loc_gln','address','zip','state']
        # fields="__all__"
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id','customer_id','gtin_number','imn','created_by','name']
class ShipPOSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShipPO
        fields="__all__"
        # fields = ["id","shipping_order_name","source_location","destination_location","subject_name","shipping_date","batch_for_export","created_by"]
class ProductionOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductionOrder
        # fields =['id','process_order_number','serialnoprovider','batch_number','manufacturing_location','product_conn','Production_line_id','regulation','production_date',
        # 'expiration_date','packaging_Version','created_by','status','requested','produced']
        fields="__all__"
class BarCodeTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =BarCodeType
        fields = "__all__"
class SnProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =SnProvider
        fields = "__all__"
class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Stock
        fields = ["id","productionorder_num","batch_num","product_name","created_by"]