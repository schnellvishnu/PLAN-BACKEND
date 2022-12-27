from masterapp.models import Company,Customers,BarCodeType,SnProvider, Stock,Locations,ShipPO,ProductionOrder,Product
from rest_framework import serializers
class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Company
        fields = ['id','company_name','created_by','address','state','zip','gln']
class CompanyErpSerializer(serializers.ModelSerializer):
                        
    class Meta:
        model =Company
        # fields="__all__"
        fields = ['id','erp','sap_client','sap_service','sap_destination','sap_language','sap_password','sap_pool_size','sap_server_host','sap_system_id','sap_sytem_number','sap_user']
        
        
class CompanyPropertySerializer(serializers.ModelSerializer):
                        
    class Meta:
        model =Company
        fields = ['id','central_repository_api_secret','gs1_company_prefix','gln','landmark','sgln_extension','to_businessparty_lookupfield','tracelink_file_receiver']
        
                
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
 
 
class ProductPropertySerializer(serializers.ModelSerializer):
                        
    class Meta:
        model = Product
        fields = ['id','GS1_company_prefix','AT_PZN','BE_ABP_CODE','BR_An_visa_Registration_Number','CA_DN',
                   'CH_Swillme_dic','CN_Subtype_Code','DE_PPN','DE_PZN','Dosage',
                    'EAN_13','Form_type','Generic_Name','GR_EOF_CODE','HR_Croatia_National_Code',
                    'IN_Product_Code','IT_Bollino','KR_KFDA_Code','License_Number','Manufacturing_Date',
                    'NL_KLMP','NRD_Nordic_VNR_Drug_Code','Packet_type','Revision_Number','PT_Aim_Number']
        
        # ,
        # ,,,,
        #          ,,
        # ]
        #         ,,]       
class ShipPOSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShipPO
        fields="__all__"
        # fields = ["id","shipping_order_name","source_location","destination_location","subject_name","shipping_date","batch_for_export","created_by"]
        
class ShipPOPropertySerializer(serializers.ModelSerializer):
                        
    class Meta:
        model = ShipPO
        fields=["id","batch_for_export","exempted_from_barcoding","exemption_notification_and_date","sold_to","advance_ship_notice"] 
              
class ProductionOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductionOrder
        # fields =['id','process_order_number','serialnoprovider','batch_number','manufacturing_location','product_conn','Production_line_id','regulation','production_date',
        # 'expiration_date','packaging_Version','created_by','status','requested','produced']
        fields="__all__"
        
        
        
class ProductionOrderPropertySerializer(serializers.ModelSerializer):
                        
    class Meta:
        model = ProductionOrder
        # fields =['id','process_order_number','serialnoprovider','batch_number','manufacturing_location','product_conn','Production_line_id','regulation','production_date',
        # 'expiration_date','packaging_Version','created_by','status','requested','produced']
        fields=["id","generic_name","composition","scheduled","usage","remark"]
   
        
                
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