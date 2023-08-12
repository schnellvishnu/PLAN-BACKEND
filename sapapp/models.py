from django.db import models

# Create your models here
from django.db import models

# from productionlineapp.models import RegisteredSystem

# Create your models here.
system_type_choices = (('system_pc','system_pc'),('ipc','ipc'))
batch_status =(('Draft','Draft'), ('Inproduction','Inproduction'),('Running','Running')
        ,('Paused','Paused'), ('Shipping','Shipping'),('InShipping','InShipping'),  ('Closed','Closed'), ('Fullyreleased','Fullyreleased'),)
class SapmanufacturingLocations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=22,unique=True)
    gln_number = models.CharField(max_length=22)
    address = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    created_by = models.CharField(max_length =100)
    status = models.BooleanField(default=False)
  

    def __str__(self):
        return self.name or ' '

class SapregisteredSystem(models.Model):
    class Meta:
        db_table = 'SapregisteredSystem'
       
    id = models.AutoField(primary_key=True)
    manufacturinglocation_id = models.ForeignKey(SapmanufacturingLocations,related_name='manufactorlocation_to_productionline',on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=40,unique=True)
    type = models.CharField(max_length=20,choices=system_type_choices)
    system_name = models.CharField(max_length=40) 
    line = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length =100)
    status = models.BooleanField(default=False)

   

    def __str__(self):
        return self.name or ''
# #---------------------------------------------------------
class Sapcustomers(models.Model):
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
    # group = models.CharField(max_length=40,choices= group_choices,null=True,blank=True)
    status= models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Saplocations(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Sapcustomers,related_name='customers_to_locations',on_delete=models.CASCADE)
    created_by = models.CharField(max_length =100,default=True)
    name = models.CharField(max_length=40,default=True)
    loc_gln = models.CharField(max_length=20,unique=True)
    ShipToLocationLookupid = models.CharField(max_length=50,default=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=100,default=True)
    country = models.CharField(max_length=20,default=True)
    state = models.CharField(max_length=20,default=True)
    city = models.CharField(max_length=20,default=True) 
    zip = models.CharField(max_length=20,default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

#     # history =  HistoricalRecords()
   
    def __str__(self):
        return self.name 
    

class Sapproduct(models.Model):
    
    name = models.CharField(max_length=100, unique= True)
    gtin_number = models.CharField(max_length=20, unique= True)
    imn = models.CharField(max_length= 20, unique= True)
    description = models.TextField(blank= True, null= True)
    created_by = models.CharField(max_length =100)
    customer_id = models.ForeignKey(Sapcustomers, related_name='customers_to_product', on_delete=models.CASCADE)
    Serial_Num_Provider_name = models.CharField(max_length= 40)
    Barcode_type_name = models.CharField(max_length= 20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status =models.BooleanField(default=False)
    item_reference = models.CharField(max_length=40)

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
    Manufacturing_Date = models.DateField(null=True)
    NL_KLMP = models.CharField(max_length=100,null=True,blank=True)
    NRD_Nordic_VNR_Drug_Code = models.CharField(max_length=100,null=True,blank=True)
    Packet_type = models.CharField(max_length=100,null=True,blank=True)
    Revision_Number = models.CharField(max_length=100,null=True,blank=True)
    PT_Aim_Number = models.CharField(max_length=100,null=True,blank=True)



    def __str__(self):
        return self.name   
      
class Sapproductionorder(models.Model):
  
    process_order_number = models.CharField(max_length= 20, unique= True)
    created_by = models.CharField(max_length =100)
    product_conn = models.ForeignKey(Sapproduct, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    batch_number = models.CharField(max_length=20,unique=True)
    manufacturing_location = models.CharField(max_length=40)
    gln_number =models.CharField(max_length=40,unique=True,null=True)
    Production_line= models.ForeignKey(SapregisteredSystem, related_name='productionline_to_batch', on_delete=models.CASCADE)
    # product_identifier = models.CharField(max_length=100)
    regulation = models.CharField(max_length=100,default="reg")
    production_date =models.DateField(null=True)
    requested  = models.IntegerField(default=0)
    produced = models.IntegerField(default=0)
    status = models.CharField(max_length=20,default='Draft')
    create_shippo = models.BooleanField(default=False)
    packaging_Version = models.CharField(max_length=40,null=True)
    expiration_date = models.DateField(null=True)
    quantity= models.CharField(max_length=20,null=True)
    gtin_number = models.CharField(max_length=20,null=True,blank=True)
    # serial_num_pool_id = models.CharField(max_length=100)  # serialnumbers_model_id
    generic_name = models.CharField(max_length=50,null=True,blank=True)
    composition = models.CharField(max_length=100,null=True,blank=True)
    scheduled = models.DateTimeField(null=True,blank=True)
    usage = models.CharField(max_length=100,null=True,blank=True)
    remark = models.CharField(max_length=100,null=True,blank=True)
    product_Image = models.ImageField(null=True,blank=True)
    wholesalers=models.CharField(max_length=50,default="dabour")
    serialnoprovider=models.CharField(max_length=60,default="Tracelink")
    Markets=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True)
    Barcodetypename = models.CharField(max_length=20, unique= True, null=True)
    model_name = models.CharField(max_length=50,null=True,blank=True)
    stock_quantity= models.CharField(max_length=50,null=True)
    shipped= models.CharField(max_length=50,null=True)
    imn=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.manufacturing_location
      