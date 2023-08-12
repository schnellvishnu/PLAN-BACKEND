from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.db import models

# Create your views here.
system_type_choices = (('system_pc','system_pc'),('ipc','ipc'))
custom_user_model = get_user_model()

class ManufacturingLocations(models.Model):
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
# ----------------------------------------------------------
class RegisteredSystem(models.Model):
    class Meta:
        db_table = 'RegisteredSystem'
        constraints = [
        models.UniqueConstraint(fields=['manufacturinglocation_id','name'], name='oneproline')
    ]
    id= models.AutoField(primary_key=True)
    manufacturinglocation_id = models.ForeignKey(ManufacturingLocations,related_name='manufactorlocation_to_productionline',on_delete=models.CASCADE)
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
#---------------------------------------------------------

class Task(models.Model)   :
    '''
    Task created on send to production (requested -date - time -requested user) 
    Task will be closed on AddJob from Productionline(closed-date-time-closed user)
    '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description= models.CharField(max_length=100)
    created_by = models.CharField(max_length =100)
    updated_by  = models.ForeignKey(custom_user_model,related_name='user_to_task_update',default=1,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_by = models.ForeignKey(custom_user_model,related_name='user_to_taskclosed',on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.title
