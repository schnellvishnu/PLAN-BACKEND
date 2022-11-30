from enum import unique
from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from datetime import datetime 
from django.contrib.auth import get_user_model
from datetime import date
# Create your models here.
user_login_status_choices = (('Locked','Locked'), ('UnLocked','UnLocked'))
user_type = (('plantserver','plantserver'),('applicationserver','applicationserver'),
			('reportserver','reportserver'))
permission_choices = (('GET','GET'), ('RETRIEVE','RETRIEVE'),('CONFIRM','CONFIRM'),
						('POST','POST'), ('PUT','PUT'),('DELETE','DELETE'),('PATCH','PATCH'))



                       
class AuditLog(models.Model):
    id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=50,null=True,blank=True)
    model_object_id = models.CharField(max_length=20,null=True,blank=True)
    history_event = models.CharField(max_length=100,null=True,blank=True)
    history_message = models.CharField(max_length=100,null=True,blank=True)
    history_date = models.DateTimeField()
    changed_by = models.IntegerField(null=True,blank=True)
    changed_fields = models.JSONField(null=True,blank=True)
    
    def __str__(self) :
    		return self.model_name

class UserRole(models.Model):

	role_name =models.CharField(max_length= 30, unique = True)
	#role_permissions = models.ManyToManyField(PermissionsList)
	role_type = MultiSelectField(max_length=50,choices=user_type)	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_by = models.CharField(max_length =100) # custom value insertion at post method in view.
	def __str__(self):
    		return self.role_name
class AppGetTracker(models.Model):
    id = models.AutoField(primary_key=True)
    app_event = models.CharField(max_length=100,null=True,blank=True)
    app_message = models.CharField(max_length=100,null=True,blank=True)
    created_by = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
# class Reg(models.Model):
#     id = models.AutoField(primary_key=True)
#     Name=models.CharField(max_length=100)
#     datebirth = models.DateField()
#     age=models.CharField(max_length=10)
#     place=models.CharField(max_length=100)
#     email=models.EmailField(max_length=100)
#     address=models.TextField()
#     mobile=models.CharField(max_length=100)
#     date_join=models.DateTimeField()
#     educational_qualification=models.CharField(max_length=100)
#     user_role= models.CharField(max_length=100)
#     username=models.CharField(max_length=100,unique=True)
#     password=models.CharField(max_length=100)
#     confirm_password=models.CharField(max_length=100)
#     #image=models.ImageField(upload_to='uploads/images',null=False,blank=False)
#     dummy1=models.CharField(max_length=100,null=True,blank=True)
#     dummy2=models.CharField(max_length=100,null=True,blank=True)
#     dummy3=models.CharField(max_length=100,null=True,blank=True)
#     dummy4=models.CharField(max_length=100,null=True,blank=True)
#     def __str__(self):
#         return self.Name
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    date_birth=models.DateField(null=True)
    age=models.CharField(max_length=100,default="age")
    place=models.CharField(max_length=100,default="place")
    email=models.EmailField(max_length=100,unique=True)
    address=models.TextField(default="address")
    mobile=models.CharField(max_length=100,default="phone")
    date_join=models.DateField(null=True)
    eduqu=models.CharField(max_length=100,default="qualification")
    userRole=models.CharField(max_length=100,default='admin')
    username=models.CharField(max_length=100,default="username")
    password=models.CharField(max_length=100,default="password")
    conpass=models.CharField(max_length=100,default="confirm password")
    dummy1=models.CharField(max_length=100,default="dummy1")
    dummy2=models.CharField(max_length=100,default="dummy2")
    dummy3=models.CharField(max_length=100,default="dummy3")
    dummy4=models.CharField(max_length=100,default="dummy4")
    key = models.CharField(max_length=500, default="key")


    
    
    
