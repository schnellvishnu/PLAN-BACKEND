
from django.db import models
from django.db.models.fields.json import JSONField
from productionlineapp.models import RegisteredSystem
group_choices = ( ('CMO','CMO'),('CPO','CPO'),('Customer','Customer'),('Destroyer','Destroyer'),('Hospital','Hospital')
                    ,('Manufacture','Manufacture'),('Pharmacy','Pharmacy'),('Transporter','Transporter'),('Warehouse','Warehouse')
                    ,('Wholesaler','Wholesaler'))
batch_status =(('Draft','Draft'), ('Inproduction','Inproduction'),('Running','Running')
        ,('Paused','Paused'), ('Shipping','Shipping'),('InShipping','InShipping'),  ('Closed','Closed'), ('Fullyreleased','Fullyreleased'),)
# Create your models here.
import uuid
import os
def get_upload_path(instance , filename):
        return os.path.join(str(instance.folder.uid) , filename)
    
class BarCodeType(models.Model):
    id = models.AutoField(primary_key=True)
    Barcodetypename = models.CharField(max_length=20, unique= True)
    labelxml = models.FileField(null=True)
    constant_encoding_fields = JSONField(null = True, blank = True)
    nonconstant_encoding_fields = JSONField(null= True, blank = True)
    nonconstant_nonencoding_fields = JSONField(null= True, blank = True)
    variable_fields = JSONField(null= True, blank= True)
    display_only_fields = JSONField(null= True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length =100)

    def __str__(self) -> str:
        return self.Barcodetypename
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city=models.CharField(max_length=20,null=True)
    country = models.CharField(max_length=20)
    created_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
    created_by = models.CharField(max_length =100)
    central_repository_api_secret = models.CharField(max_length=100)
    gln = models.CharField(max_length=20)
    gs1_company_prefix = models.CharField(max_length=20)
    landmark = models.CharField(max_length=20,null=True,blank=True)
    sgln_extension = models.CharField(max_length=100)
    to_businessparty_lookupfield = models.CharField(max_length=20)
    tracelink_file_receiver = models.CharField(max_length=100)
    
    title=models.CharField(max_length=100,null=True)
    url=models.URLField(null=True)
    tracelink_username=models.CharField(max_length=100,default=True)
    siteid=models.IntegerField(null=True)
    sftp_port=models.IntegerField(null=True)
    sftp_password=models.CharField(max_length=100,default="password")
    file_sender=models.CharField(max_length=100,default=True)
    sending_system=models.CharField(max_length=100,default="system1")
    tracelink_password=models.CharField(max_length=100,default="password")
    sftp_host=models.CharField(max_length=100,null=True)
    sftp_username=models.CharField(max_length=100,default=True)
    file_receiver=models.CharField(max_length=100,null=True)
    
    
    erp = models.CharField(max_length=100,null=True,blank=True)
    sap_client = models.CharField(max_length=100,null=True,blank=True)
    sap_service =models.CharField(max_length=100,null=True,blank=True)
    sap_destination =models.CharField(max_length=100,null=True,blank=True)
    sap_language =models.CharField(max_length=100,null=True,blank=True)
    sap_password =models.CharField(max_length=100,null=True,blank=True)
    sap_pool_size =models.CharField(max_length=100,null=True,blank=True)
    sap_server_host =models.CharField(max_length=100,null=True,blank=True)
    sap_system_id =models.CharField(max_length=100,null=True,blank=True)
    sap_sytem_number =models.CharField(max_length=100,null=True,blank=True)
    sap_user =models.CharField(max_length=100,null=True,blank=True)
    
    
    
    
     
    def __str__(self) :
        return self.company_name

class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    created_by = models.CharField(max_length =100)
    company_prefix  = models.CharField(max_length=20)
    company_gln  = models.CharField(max_length=20)
    description = models.TextField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20) 
    zip = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ShipToLocationLookupid = models.CharField(max_length=100,null=True,blank=True)
    group = models.CharField(max_length=40,choices= group_choices,null=True,blank=True)
    status= models.BooleanField(default=False)
    # status=models.CharField(max_length=100,default="Not Confirmed")
    landmark=models.CharField(max_length=100,null=True)
    sgln_extension=models.CharField(max_length=100,null=True)
    tobusinessparylookupid=models.CharField(max_length=100,null=True)
    
    title=models.CharField(max_length=100,null=True)
    url=models.URLField(null=True)
    tracelink_username=models.CharField(max_length=100,default=True)
    siteid=models.IntegerField(null=True)
    sftp_port=models.IntegerField(null=True)
    sftp_password=models.CharField(max_length=100,default="password")
    file_sender=models.CharField(max_length=100,default=True)
    sending_system=models.CharField(max_length=100,default="system1")
    tracelink_password=models.CharField(max_length=100,default="password")
    sftp_host=models.CharField(max_length=100,null=True)
    sftp_username=models.CharField(max_length=100,default=True)
    file_receiver=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Locations(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customers,related_name='customers_to_locations',on_delete=models.CASCADE)
    created_by = models.CharField(max_length =100)
    name = models.CharField(max_length=40)
    loc_gln = models.CharField(max_length=20,unique=True)
    ShipToLocationLookupid = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20) 
    zip = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    district=models.CharField(max_length=100,null=True)
    ship_to_locationlookup_id=models.CharField(max_length=100,null=True)
    tracelink_file_sender=models.CharField(max_length=100,null=True)
    sgln_extension=models.CharField(max_length=100,null=True) 

    # history =  HistoricalRecords()

    def __str__(self):
        return self.name 
   
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    gtin_number = models.CharField(max_length=20, unique= True)
    imn = models.CharField(max_length= 20, unique= True)
    description = models.TextField(blank= True, null= True)
    created_by = models.CharField(max_length =100)
    customer_id = models.ForeignKey(Customers, related_name='customers_to_product', on_delete=models.CASCADE)
   
    Barcode_type_name = models.CharField(max_length= 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status =models.BooleanField(default=False)
    # status=models.CharField(max_length=100,default="Not Confirmed")
    item_reference = models.CharField(max_length=40)
    
    finished_good_code= models.CharField(max_length=100,null=True,blank=True)
    location_code=models.CharField(max_length=100,null=True,blank=True)
    regulation=models.CharField(max_length=100,null=True,blank=True)
    sscc_prn=models.CharField(max_length=100,null=True,blank=True)
    Serial_Num_Provider_name = models.CharField(max_length=40,null=True,blank=True)
    
    
    GS1_company_prefix = models.CharField(max_length=100,null=True,blank=True)
    AT_PZN = models.CharField(max_length=100,null=True,blank=True)
    BE_ABP_CODE = models.CharField(max_length=100,null=True,blank=True)
    BR_An_visa_Registration_Number = models.CharField(max_length=100,null=True,blank=True)
    CA_DN = models.CharField(max_length=100,null=True,blank=True)
    CH_Swillme_dic = models.CharField(max_length=100, null=True,blank=True)
    CN_Subtype_Code = models.CharField(max_length=100, null=True,blank=True)
    DE_PPN = models.CharField(max_length=100,null=True,blank=True)
    DE_PZN = models.CharField(max_length=100,null=True,blank=True)
    Dosage = models.CharField(max_length=100,null=True,blank=True)
    EAN_13 = models.CharField(max_length=100,null=True,blank=True)
    
    Form_type = models.CharField(max_length=100,null=True,blank=True)
    Generic_Name = models.CharField(max_length=100,null=True,blank=True)
    GR_EOF_CODE = models.CharField(max_length=100,null=True,blank=True)
    HR_Croatia_National_Code = models.CharField(max_length=100,null=True,blank=True)
    IN_Product_Code = models.CharField(max_length=100,null=True,blank=True)
    IT_Bollino = models.CharField(max_length=100,null=True,blank=True)
    KR_KFDA_Code = models.CharField(max_length=100,null=True,blank=True)
    License_Number = models.CharField(max_length=100,null=True,blank=True)
    Manufacturing_Date = models.DateField(null=True,blank=True)
    NL_KLMP = models.CharField(max_length=100,null=True,blank=True)
    NRD_Nordic_VNR_Drug_Code = models.CharField(max_length=100,null=True,blank=True)
    Packet_type = models.CharField(max_length=100,null=True,blank=True)
    Revision_Number = models.CharField(max_length=100,null=True,blank=True)
    PT_Aim_Number = models.CharField(max_length=100,null=True,blank=True)
    
    hrf1= models.CharField(max_length=100,null=True,blank=True)
    hrf2= models.CharField(max_length=100,null=True,blank=True)
    hrf3= models.CharField(max_length=100,null=True,blank=True)
    hrf4= models.CharField(max_length=100,null=True,blank=True)
    hrf5= models.CharField(max_length=100,null=True,blank=True)
    hrf6= models.CharField(max_length=100,null=True,blank=True)
    
    
    markets = models.JSONField(blank=True, default="[{\"markets_name\":\"India\",\"checkedStatus\":false}]")
    
    
   
    def __str__(self):
        return self.name 
    
class Markets(models.Model):
     id=models.AutoField(primary_key=True)
     markets_name=models.CharField(max_length=100,unique=True)
     
     def __str__(self):
         return self.markets_name                       
    
class ProductionOrder(models.Model):
                        
    def namefile(instance,filename):
        return '/'.join(['image',str(instance.manufacturing_location),filename])                    
    id = models.AutoField(primary_key=True)
    process_order_number = models.CharField(max_length= 20, unique= True)
    created_by = models.CharField(max_length =100)
    product_conn = models.ForeignKey(Product, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    batch_number = models.CharField(max_length=20,unique=True)
    manufacturing_location = models.CharField(max_length=40)
    gln_number =models.CharField(max_length=40,unique=True,null=True)
    Production_line_id = models.ForeignKey(RegisteredSystem, related_name='productionline_to_batch', on_delete=models.CASCADE)
    # product_identifier = models.CharField(max_length=100)
    regulation = models.CharField(max_length=100,default=True)
    production_date =models.DateField(null=True)
    requested  = models.IntegerField(default=0)
    produced = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices = batch_status,default='Draft')
    create_shippo = models.BooleanField(default=False)
    packaging_Version = models.CharField(max_length=40,null=True)
    expiration_date = models.DateField(null=True)
    serialnoprovider=models.CharField(max_length=60,default="Tracelink")
    quantity= models.CharField(max_length=20,null=True)
    gtin_number = models.CharField(max_length=20,null=True,blank=True)
    # serial_num_pool_id = models.CharField(max_length=100)  # serialnumbers_model_id
    generic_name = models.CharField(max_length=50,null=True,blank=True)
    composition = models.CharField(max_length=100,null=True,blank=True)
    scheduled = models.DateField(max_length=100,null=True,blank=True)
    usage = models.CharField(max_length=100,null=True,blank=True)
    remark = models.CharField(max_length=100,null=True,blank=True)
    product_Image = models.ImageField(upload_to=namefile,null=True,blank=True)
    wholesalers=models.CharField(max_length=50,default="dabour")

    Markets=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True)
    Barcodetypename = models.CharField(max_length=20, unique= True, null=True)
    model_name = models.CharField(max_length=50,null=True,blank=True)
    stock_quantity= models.CharField(max_length=50,null=True)
    shipped= models.CharField(max_length=50,null=True)
    identifier=models.CharField(max_length=100,unique=True,null=True)
    line=models.CharField(max_length=100,null=True,blank=True)
    type=models.CharField(max_length=100,null=True,blank=True)
    
    
    AT_PZN = models.CharField(max_length=100,null=True,blank=True)
    BE_ABP_CODE = models.CharField(max_length=100,null=True,blank=True)
    BR_An_visa_Registration_Number = models.CharField(max_length=100,null=True,blank=True)
    CA_DN = models.CharField(max_length=100,null=True,blank=True)
    CH_Swillme_dic = models.CharField(max_length=100, null=True,blank=True)
    CN_Subtype_Code = models.CharField(max_length=100, null=True,blank=True)
    DE_PPN = models.CharField(max_length=100,null=True,blank=True)
    DE_PZN = models.CharField(max_length=100,null=True,blank=True)
    Dosage = models.CharField(max_length=100,null=True,blank=True)
    EAN_13 = models.CharField(max_length=100,null=True,blank=True)
    Form_type = models.CharField(max_length=100,null=True,blank=True)
    Generic_Name = models.CharField(max_length=100,null=True,blank=True)
    GR_EOF_CODE = models.CharField(max_length=100,null=True,blank=True)
    HR_Croatia_National_Code = models.CharField(max_length=100,null=True,blank=True)
    IN_Product_Code = models.CharField(max_length=100,null=True,blank=True)
    internal_material_number=models.CharField(max_length=100,unique=True,blank=True)
    IT_Bollino = models.CharField(max_length=100,null=True,blank=True)
    KR_KFDA_Code = models.CharField(max_length=100,null=True,blank=True)
    License_Number = models.CharField(max_length=100,null=True,blank=True)
    Manufacturing_Date = models.DateField(null=True)
    NL_KLMP = models.CharField(max_length=100,null=True,blank=True)
    NRD_Nordic_VNR_Drug_Code = models.CharField(max_length=100,null=True,blank=True)
    Packet_type = models.CharField(max_length=100,null=True,blank=True)
    Revision_Number = models.CharField(max_length=100,null=True,blank=True)
    PT_Aim_Number = models.CharField(max_length=100,null=True,blank=True)
    
    # hrf1=models.JSONField(default={'null':'null'})
    # hrf2=models.JSONField(default={'null':'null'})
    # hrf3=models.JSONField(default={'null':'null'})
    # hrf4=models.JSONField(default={'null':'null'})
    # hrf5=models.JSONField(default={'null':'null'})
    # hrf6=models.JSONField(default={'null':'null'})
    hrf= models.JSONField(max_length=200,null=True,blank=True)
    
    
    def __str__(self):
        return self.manufacturing_location     

class ShipPO(models.Model):
    id = models.AutoField(primary_key=True)
    shipping_order_name = models.CharField(max_length=40)
    process_order_number=models.ForeignKey(ProductionOrder,related_name='processorderno_to_shippo',on_delete=models.CASCADE)
    source_location = models.ForeignKey(Locations,related_name='location_to_shippo',on_delete=models.CASCADE)
    destination_location = models.ForeignKey(Locations,related_name='locations_to_shipping',on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Customers,related_name='customers_to_shippingpo',on_delete=models.CASCADE)
    shipping_date = models.DateField(null=True)
    shipping_time=models.TimeField(null=True)
    status = models.CharField(max_length=20, choices = batch_status,default='Shipping') # false = stock and true = shipped
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length =100)
    shipping_type = models.CharField(max_length=20,default='item')
    batch_for_export = models.CharField(max_length=100,null=True)
    exempted_from_barcoding = models.CharField(max_length=100,null=True,blank=True)
    exemption_notification_and_date = models.CharField(max_length=100,null=True,blank=True)
    exempted_country_code = models.CharField(max_length=100,null=True,blank=True)
    sold_to = models.CharField(max_length=100,null=True,blank=True)
    delivery_number = models.CharField(max_length=100,null=True,blank=True)
    # delivary_number equals to  advance_ship_notice are Batch number
    delivary_number = models.CharField(max_length=100,null=True,blank=True)
    advance_ship_notice = models.CharField(max_length=100,null=True,blank=True)
    process_no_original=models.IntegerField(null=True)

    def __str__(self) :
        return self.shipping_order_name

class SnProvider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length =100)
    requested_link = models.CharField(max_length=100,null=True,blank=True)
    requested_xml = models.TextField(null=True,blank=True)
    commisioning_link = models.CharField(max_length=100,null=True,blank=True)
    commisioning_xml = models.TextField(null=True,blank=True)
    aggregation_link = models.CharField(max_length=100,null=True,blank=True)
    aggregation_xml = models.TextField(null=True,blank=True)
    destroy_link = models.CharField(max_length=100,null=True,blank=True)
    destroy_xml = models.TextField(null=True,blank=True)
    shipping_link = models.CharField(max_length=100,null=True,blank=True)
    shipping_xml = models.TextField(null=True,blank=True)
    status = models.BooleanField(default=False)
    extrafield=models.CharField(max_length=14,default="")

    def __str__(self) -> str:
        return self.name
    
# class Tracelinksettings(models.Model):
#       id=models.AutoField(primary_key=True)
#       title=models.CharField(max_length=100,null=True)
#       url=models.URLField(null=True)
#       tracelink_username=models.CharField(max_length=100,default=True)
#       siteid=models.IntegerField(null=True)
#       sftp_port=models.IntegerField(null=True)
#       sftp_password=models.CharField(max_length=100,default="password")
#       file_sender=models.CharField(max_length=100,default=True)
#       sending_system=models.CharField(max_length=100,default="system1")
#       tracelink_password=models.CharField(max_length=100,default="password")
#       sftp_host=models.CharField(max_length=100,null=True)
#       sftp_username=models.CharField(max_length=100,default=True)
#       file_receiver=models.CharField(max_length=100,null=True)
#       def __str__(self) -> str:
#             return self.title                  

class Stock(models.Model):  
    id = models.AutoField(primary_key=True)  
    process_order_number = models.CharField(max_length=100)
    product_conn = models.CharField(max_length=100)
    created_by = models.CharField(max_length =100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    batch_number = models.CharField(max_length=50)
    requested = models.CharField(max_length=50)
    stock_quantity = models.CharField(max_length=50)#produced
    shipped = models.CharField(max_length=50)
    removed = models.CharField(max_length=50)
    standard= models.CharField(max_length=250)
    expiration_date = models.CharField(max_length=250)
    
# class Erpsetting(models.Model):
#     id = models.AutoField(primary_key=True)
#     erp = models.CharField(max_length=100,null=True,blank=True)
#     sap_client = models.CharField(max_length=100,null=True,blank=True)
#     sap_service =models.CharField(max_length=100,null=True,blank=True)
#     sap_destination =models.CharField(max_length=100,null=True,blank=True)
#     sap_language =models.CharField(max_length=100,null=True,blank=True)
#     sap_password =models.CharField(max_length=100,null=True,blank=True)
#     sap_pool_size =models.CharField(max_length=100,null=True,blank=True)
#     sap_server_host =models.CharField(max_length=100,null=True,blank=True)
#     sap_system_id =models.CharField(max_length=100,null=True,blank=True)
#     sap_sytem_number =models.CharField(max_length=100,null=True,blank=True)
#     sap_user =models.CharField(max_length=100,null=True,blank=True)
    
#     def __str__(self) -> str:
#         return self.erp
    
# class Gtins(models.Model):
#                         # pro_details_gtin = models.ForeignKey(Product,related_name='product_to_gtins',on_delete=models.CASCADE)    
#     # Snum_Provider_id = models.ForeignKey(SnProvider,related_name='snprovider_to_gtins',on_delete=models.CASCADE)
   
#     gtin = models.ForeignKey(Product, on_delete= models.CASCADE)
#     available_quantity = models.PositiveIntegerField(default=0)
#     minimum_quantity = models.PositiveIntegerField()
#     renewal_quantity = models.PositiveIntegerField()
#     '''locked becomes True when deleting the gtin only developer can change back to false'''
#     # locked = models.BooleanField(default=False)
#     last_log = models.DateTimeField(auto_now=True)
#     failed_attempts = models.CharField(max_length=10)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_by = models.CharField(max_length =100)
#     status= models.BooleanField(default=False)
   

#     def __str__(self):
#         return str(self.gtin)
    
class Gtins(models.Model):
                        # pro_details_gtin = models.ForeignKey(Product,related_name='product_to_gtins',on_delete=models.CASCADE)    
    # Snum_Provider_id = models.ForeignKey(SnProvider,related_name='snprovider_to_gtins',on_delete=models.CASCADE)
   
    # gtin = models.ForeignKey(Product, on_delete= models.CASCADE)
    gtin=models.CharField(max_length=100,unique= True,null=True)
    
    available_quantity = models.PositiveIntegerField(default=0)
    
    minimum_quantity = models.PositiveIntegerField()
    renewal_quantity = models.PositiveIntegerField()
    '''locked becomes True when deleting the gtin only developer can change back to false'''
    # locked = models.BooleanField(default=False)
    last_log = models.DateTimeField(auto_now=True)
    failed_attempts = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length =100)
    status= models.BooleanField(default=False)
    #numbers=models.TextField(max_length=10000,default=True)
    numbers=models.JSONField(max_length=200,null=True,blank=True)
    snnumbers=models.CharField(max_length=100,default=True)
    
   

    def __str__(self):
        return str(self.gtin)
                 



class PrinterdataTable(models.Model):
                        
        id=models.AutoField(primary_key=True)
        processordernumber=models.CharField(max_length=100,unique= True)
        # serialnumberjson=models.TextField(max_length=10000,null=True,blank=True)
        
      
        
        expiration_date = models.DateField(null=True)
        # gtin = models.ForeignKey(Gtins, on_delete= models.CASCADE)
        lot=models.CharField(max_length=100,null=True)
        gtin=models.CharField(max_length=100,unique= True,null=True)
        numbers=models.JSONField(null=True,blank=True)
        quantity= models.CharField(max_length=20,null=True)
        hrf= models.JSONField(null=True,blank=True)
        type=models.CharField(max_length=100,null=True)
        
        
        def __str__(self):
                return str(self. id)

class Downloadcodes(models.Model):
    id=models.AutoField(primary_key=True)
    process_order_number = models.CharField(max_length= 20, unique= True,null=True)
    serialnumberwithgtin=models.JSONField(null=True,blank=True) 
    def __str__(self):
            return str(self. id)  
