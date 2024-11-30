from masterapp.models import Company,Customers,BarCodeType,SnProvider, Stock,Locations,ShipPO,ProductionOrder,Product,Markets,Gtins,SnProvider,PrinterdataTable,Downloadcodes,ProdReport,Allocatednumbers
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Company
        fields = ['id','company_name','created_by','address','state','zip','gln','city','country','companyflag']
class CompanyErpSerializer(serializers.ModelSerializer):
                        
    class Meta:
        model =Company
        # fields="__all__"
        fields = ['id','erp','sap_client','sap_service','sap_destination','sap_language','sap_password','sap_pool_size','sap_server_host','sap_system_id','sap_sytem_number','sap_user']
 
# class ErpSerializer(serializers.ModelSerializer):
#         class Meta:
#             model =Erpsetting
#             fields = "__all__"
                                     
class CompanyPropertySerializer(serializers.ModelSerializer):
                        
    class Meta:
        model =Company
        fields = ['id','central_repository_api_secret','gs1_company_prefix','gln','landmark','sgln_extension','to_businessparty_lookupfield','tracelink_file_receiver']
        
        
class CompanyTracelinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=['id','title','url','tracelink_username','siteid','sftp_port','sftp_password','file_sender','sending_system','tracelink_password','sftp_host','sftp_username','file_receiver']        
                       
class CustomersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Customers
        fields =['id','name','created_by','address','zip','group','country','state','city','status','customerflag']
        # fields="__all__"
        
class CustomersPropertySerializer(serializers.ModelSerializer):
                        
    class Meta:
        model =Customers
        fields =['id','company_prefix','company_gln','landmark','sgln_extension','tobusinessparylookupid','file_receiver']                
        
class CustomerTracelinkSerializer(serializers.ModelSerializer):
                        class Meta:
                                model=Customers
                                fields=["id","title","url","tracelink_username","siteid","sftp_port",
                                      "sftp_password","file_sender","sending_system","tracelink_password",
                                      "sftp_host","sftp_username","file_receiver"]                        
class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Locations
        fields = ['id','customer_id','name','created_by','loc_gln','address','zip','state','city','locationflag']
        # fields="__all__"
        
class LocationPropertySerializer(serializers.ModelSerializer):
         class Meta:
            model =Locations
            fields = ['id','district','ship_to_locationlookup_id','tracelink_file_sender','loc_gln','sgln_extension']
        # fields="__all__"
                                                      
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id','customer_id','gtin_number','imn','created_by','name','status','productflag']
        

class ProductErpSerializer(serializers.ModelSerializer):
                        
        class Meta:
             model=Product
             fields=['id','finished_good_code','Serial_Num_Provider_name','item_reference','location_code','regulation','sscc_prn']                               
                         
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
        # fields = ["id","shipping_order_name","source_location","destination_location","subject_name","shipping_date","batch_for_export","created_by","shipping_time","process_order_number","status","process_no_original"]
        
class ShipPOPropertySerializer(serializers.ModelSerializer):
                        
    class Meta:
        model = ShipPO
        fields=["id","batch_for_export","exempted_from_barcoding","exemption_notification_and_date","sold_to","advance_ship_notice",'process_no_original'] 
              
class ProductionOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductionOrder
        fields =['id','process_order_number','serialnoprovider','batch_number','manufacturing_location','product_conn','Production_line_id','regulation','production_date',
        'expiration_date','packaging_Version','created_by','status','internal_material_number',"requested","produced","line","gtin_number","type","prodcutionorderflag"]
        # fields="__all__"
       
class ProductionOrderPropertySerializer(serializers.ModelSerializer):
                        
    class Meta:
        model = ProductionOrder
        # fields =['id','process_order_number','serialnoprovider','batch_number','manufacturing_location','product_conn','Production_line_id','regulation','production_date',
        # 'expiration_date','packaging_Version','created_by','status','requested','produced']
        fields=["id","generic_name","composition","scheduled","usage","remark","product_Image"]
                
class BarCodeTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =BarCodeType
        fields = "__all__"
class SnProviderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =SnProvider
        # fields = "__all__"
        fields=["id","name","extrafield"]
class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Stock
        fields = ["id","process_order_number","batch_number","product_conn","created_by"]
        

              
class MarketsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Markets
        fields="__all__"
        
class ProductHrSerializer(serializers.ModelSerializer):
                        class Meta:
                              model=Product
                              fields=["id","hrf1","hrf2","hrf3","hrf4","hrf5","hrf6"] 
                                               
class ProductMarketpageSerializer(serializers.ModelSerializer):
                        class Meta:
                              model=Product
                              fields=["id","markets"]                  


class ProductionorderHrfSerializer(serializers.ModelSerializer):
                        class Meta:
                              model=ProductionOrder
                              fields=["id","hrf"] 
                                               
class  GtinsSerializer(serializers.ModelSerializer):
                        class Meta:
                                model=Gtins 
                                fields=["id","gtin","available_quantity"]               


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrinterdataTable
        fields=["id","numbers","expiration_date","lot","gtin","processordernumber","quantity","hrf","type","ip_address"]  
        
class BalancedslnoSerializer(serializers.ModelSerializer):
    class Meta:
        model=PrinterdataTable
        fields=["id","gtin","balanced_serialnumbers"]          
        
             
class DownloadcodesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Downloadcodes
        fields="__all__"                      
        
class ProdReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdReport
        fields = "__all__"  
        
class AllocatednumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allocatednumbers
        fields=["id","batch_number","process_order_number","gtin_number","quantity","available_quantity","created_by"]  