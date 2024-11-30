from django.shortcuts import render
from rest_framework import generics

from accounts.models import  UserRole,AuditLog,Register,History,UserrolePermissions,UserAuditHistoryOnly,Loginmodel
from accounts.serializers import UserRoleSerializer,HistorySerializer,RegisterSerializer,UserrolePermissionsSerializer,UserHistorySerializer,LoginModelSerializer
# from masterapp.permissions import ObjectDestroyPermission, Productpermission
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts import serializers
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User
import datetime


# from django_filters.rest_framework import  DjangoFilterBackend
# from apps_extra_code.custom_list_search_filter import CustomSearchFilter



class UserroleView(APIView):
    def get(self, request):
        detailsObj = UserRole.objects.all()
        serializeObj = UserRoleSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = UserRoleSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateUserrole(APIView):
    def put(self, request, pk):
        try:
            detailObj = UserRole.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = UserRoleSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteUserrole(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = UserRole.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)

#-----------------------------------------------------------
class AuditLogView(APIView):
    def get(self, request):
        detailsObj = History.objects.all()
        serializeObj = HistorySerializer(detailsObj, many = True)
        return Response(serializeObj.data)

class HistoryemployeandmodelIndividual(APIView):
                                        
    def get(self, request,id):
        # email=request.data["email"]
                          
        detailsObj = History.objects.all().filter(donebyemployeeid=id).order_by('-id')
       
        serializeObj = HistorySerializer(detailsObj, many = True)
        return Response(serializeObj.data)
                            
        # try:
        #     detailsObj =History.objects.get(modelname=id,donebyuser=id1)
        #     serializeObj2 = HistorySerializer(detailsObj, many=True)
        # except:
        #     print("hi")
        # return Response(serializeObj2.data) 
#     def post(self, request):
#         serializeObj = AuditLogSerializer(data=request.data)
#         if serializeObj.is_valid():
#             serializeObj.save()
#             return Response(200)
#         return Response(serializeObj.errors)

# class updateAuditlog(APIView):
#     def put(self, request, pk):
#         try:
#             detailObj = AuditLog.objects.get(pk=pk)
#         except:
#             return Response("Not found in database")

#         serializeObj = AuditLogSerializer(detailObj, data=request.data)
#         if serializeObj.is_valid():
#             serializeObj.save()
#             return Response(200)
#         return Response(serializeObj.errors)
class HistoryemployeandmodelnameIndividual(APIView):
                                        
    def get(self, request,id):
        # email=request.data["email"]
                          
        detailsObj = History.objects.all().filter(modelname=id).order_by('-id')
       
        serializeObj = HistorySerializer(detailsObj, many = True)
        return Response(serializeObj.data)
    
    
                            
class deleteAuditlog(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = History.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
#----------------------------------------------------------


class UserAuditReportdate(APIView):  
    def get(self, request):
        detailsObj = UserAuditHistoryOnly.objects.all()
        serializeObj = UserHistorySerializer(detailsObj, many=True)
        # fromDate = request.data["datefrom"]
        # toDate = request.data["dateto"]
        # response  = ProductionReport.objects.filter( production_date=fromDate, production_date__lte=toDate)
        return Response(serializeObj.data)
    
    def post(self, request):
        serializeObj = UserHistorySerializer(data=request.data)
        v=[]
        startdate = request.data["datefrom"]
        
        toDate = request.data["dateto"]
        # fromDate=str(request.POST.get('datefrom'))
        # toDate=str(request.POST.get("dateto"))
        # response  =ProductionReport.objects.all().filter(production_date=id)
        
        response  =UserAuditHistoryOnly.objects.all().filter(datefield__range=(startdate,toDate) )
        serializeObj = UserHistorySerializer(response , many=True)
        return Response(serializeObj.data)

class RegisterView(APIView):

    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        detailsObj = Register.objects.all().order_by("-id")
        serializeObj =RegisterSerializer(detailsObj, many = True)
        return Response(serializeObj.data)


    def post(self, request):
            serializeObj = RegisterSerializer(data=request.data)
            if serializeObj.is_valid():
                serializeObj.save()

                #########  Registering the user in User model
                userMail = request.data['email']
                userName = request.data['Name']
                userPassword = request.data['password']
                user = User.objects.create_user(username=userMail, email=userMail, password=userPassword)
                user.save()

                return Response(200)
            return Response(serializeObj.errors)  

    # def post(self, request):
    #     serializeObj = RegisterSerializer(data=request.data)
    #     if serializeObj.is_valid():
    #         serializeObj.save()
    #         return Response(200)
    #     return Response(serializeObj.errors)



	    

class updateRegister(APIView):
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        try:
            detailObj = Register.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = RegisterSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class deleteRegister(APIView):
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            detailsObj = Register.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)

class userAuthVerify(APIView):

	# authentication_classes = [SessionAuthentication, BasicAuthentication]
	# permission_classes = [IsAuthenticated]

	def post(self, request):
            userData=Register.objects.filter(email=request.data['username']).values()
            if userData:
                return Response(userData[0]['userRole'])
            else:
                return Response("notExists")                   
		
class  Registerindividual(APIView):
    def get(self, request, id):
        detailsObj =Register.objects.all().filter(id=id)
        serializeObj = RegisterSerializer(detailsObj, many=True)
        return Response(serializeObj.data)
class RegisteremployeIndividual(APIView):
                    
    def get(self, request, id):

        detailsObj =Register.objects.all().filter(employeeid=id).order_by('-id')

        serializeObj = RegisterSerializer(detailsObj, many=True)

        return Response(serializeObj.data) 


#________________________________________________________


# class RegView(APIView):
#     def get(self, request):
#         detailsObj = Reg.objects.all()
#         serializeObj =RegSerializer(detailsObj, many = True)
#         return Response(serializeObj.data)

   
#     def post(self, request):
#         serializeObj = RegSerializer(data=request.data)
#         if serializeObj.is_valid():
#             serializeObj.save()
#             return Response(200)
#         return Response(serializeObj.errors)

# class updateReg(APIView):
#     def put(self, request, pk):
#         try:
#             detailObj = Reg.objects.get(pk=pk)
#         except:
#             return Response("Not found in database")

#         serializeObj = RegSerializer(detailObj, data=request.data)
#         if serializeObj.is_valid():
#             serializeObj.save()
#             return Response(200)
#         return Response(serializeObj.errors)

# class deleteReg(APIView):
#     def delete(self, request, pk):
#         try:
#             detailsObj = Reg.objects.get(pk=pk)
#         except:
#             return Response("Not found in database")

#         detailsObj.delete()
#         return Response(200)

class logInController(APIView): 
    def post(self, request):
        # print(request.data['username'])                   
        userData = Register.objects.filter(email=request.data['username']).values()
        
        if(userData):
            if(userData[0]['password'] == request.data['password']):
                historySave = History(modelname='Login Details',

                savedid="noid",

                operationdone='login',

                donebyuser=userData[0]['Name'],

                donebyuserrole=userData[0]['userRole'],

                donedatetime=datetime.datetime.now(),

                # historyText="Loggedin the user " +userData[0]['Name']+ ", whose role is " + userData[0]['userRole'])
                )
                historySave.save() 
                
                userhistorySave = UserAuditHistoryOnly(modelname='Login Details',

                

                operationdone='login',

                donebyuser=userData[0]['email'],

                donebyuserrole=userData[0]['userRole'],

                donedatetime=datetime.datetime.now(),

                # historyText="Loggedin the user " +userData[0]['Name']+ ", whose role is " + userData[0]['userRole'])
                )
                userhistorySave.save() 
                return Response({'userrole':userData[0]['userRole'], 'username':userData[0]['email'],'employeeid':userData[0]['employeeid']})
            else:
                return Response("passwordDoesNotMatch") 
        else:
            return Response("UserDoesNotExist")

class logoutController(APIView):
                    
    def post(self,request):

        username=request.data["username"]

        userrole=request.data["userrole"]

        historySave = History(modelname='LogOut Details',

                            savedid="noid",

                            operationdone='logout',

                            donebyuser=username,

                            donebyuserrole=userrole,

                            donedatetime=datetime.datetime.now(),

                            # historyText="Loggedout the user " +username+ ", whose role is " + userrole)
                            )
        historySave.save()
        
        userhistorySave = UserAuditHistoryOnly(modelname='Login Details',

                

                

                            operationdone='logout',

                            donebyuser=username,

                            donebyuserrole=userrole,

                            donedatetime=datetime.datetime.now(),

                # historyText="Loggedin the user " +userData[0]['Name']+ ", whose role is " + userData[0]['userRole'])
                )
        userhistorySave.save() 

        return Response(200)
class userPermissionEdit(APIView):
    def post(self, request):
        # print(request.data['userrole'])
        # print(request.data['Applicationserver_Changepassword_read'])
        # print(request.data['Applicationserver_Changepassword_create'])
        # print(request.data['Applicationserver_Changepassword_update'])
        # print(request.data['Applicationserver_Changepassword_delete'])
        Registeredusers_json = {
            'READ': request.data['Registeredusers_read'], 
            'CREATE':request.data['Registeredusers_create'], 
            'UPDATE': request.data['Registeredusers_update'],
            'DELETE':request.data['Registeredusers_delete'],         
        }
       
        Productionorder_json = {
            'READ': request.data['Productionorder_read'], 
            'CREATE':request.data['Productionorder_create'], 
            'UPDATE': request.data['Productionorder_update'],
            'DELETE':request.data['Productionorder_delete']
        }
        # SendtoShip_json = {
        #     'READ': request.data['SendtoShip_read'], 
        #     'CREATE':request.data['SendtoShip_create'], 
        #     'UPDATE': request.data['SendtoShip_update'],
        #     'DELETE':request.data['SendtoShip_delete']
        # }
        ShippingOrder_json ={
            'READ':request.data['ShippingOrder_read'],
            'CREATE':request.data['ShippingOrder_create'],
            'UPDATE':request.data['ShippingOrder_update'],
            'DELETE':request.data['ShippingOrder_delete']
        }
        Stock_json ={
          'READ':request.data['Stock_read']  
        }
        Company_json = {
            'READ': request.data['Company_read'], 
            'CREATE':request.data['Company_create'], 
            'UPDATE': request.data['Company_update'],
            'DELETE':request.data['Company_delete']
        }
        
        Customer_json = {
            'READ': request.data['Customer_read'], 
            'CREATE':request.data['Customer_create'], 
            'UPDATE': request.data['Customer_update'],
            'DELETE':request.data['Customer_delete']
        }
        
        CustomerLocation_json = {
            'READ': request.data['CustomerLocation_read'], 
            'CREATE':request.data['CustomerLocation_create'], 
            'UPDATE': request.data['CustomerLocation_update'],
            'DELETE':request.data['CustomerLocation_delete']
        }
        
        Product_json = {
            'READ': request.data['Product_read'], 
            'CREATE':request.data['Product_create'], 
            'UPDATE': request.data['Product_update'],
            'DELETE':request.data['Product_delete']
        }
        
        ManufacturingLocation_json = {
            'READ': request.data['Manufact_read'], 
            'CREATE':request.data['Manufact_create'], 
            'UPDATE': request.data['Manufact_update'],
            'DELETE':request.data['Manufact_delete']
        }
        
        
        RegisteredSystem_json = {
            'READ': request.data['RegisteredSystem_read'], 
            'CREATE':request.data['RegisteredSystem_create'], 
            'UPDATE': request.data['RegisteredSystem_update'],
            'DELETE':request.data['RegisteredSystem_delete']
        }
        
        
        History_json = {
            'READ': request.data['History_read'],  
            'DELETE':request.data['History_delete']
        }
        
        Dashboard_json = {
            'READ': request.data['Dashboard_read']  
        }
        
        SnProvider_json = {
            'READ': request.data['SnProvider_read'], 
            'CREATE':request.data['SnProvider_create'], 
            'UPDATE': request.data['SnProvider_update'],
            'DELETE':request.data['SnProvider_delete']
        }
        
        
        GtinPool_json = {
            'READ': request.data['Gtinpool_read'], 
            'CREATE':request.data['Gtinpool_create'], 
            'UPDATE': request.data['Gtinpool_update'],
            'DELETE':request.data['Gtinpool_delete']
        }
        
        Auditreport_json = {
            'READ': request.data['Auditreport_read'], 
            'CREATE':request.data['Auditreport_create'], 
            'UPDATE': request.data['Auditreport_update'],
            'DELETE':request.data['Auditreport_delete']
        }
        
        Shippingreport_json = {
            'READ': request.data['Shippingreport_read'], 
            'CREATE':request.data['Shippingreport_create'], 
            'UPDATE': request.data['Shippingreport_update'],
            'DELETE':request.data['Shippingreport_delete']
        }
        
        Productionreport_json = {
            'READ': request.data['Productionreport_read'], 
            'CREATE':request.data['Productionreport_create'], 
            'UPDATE': request.data['Productionreport_update'],
            'DELETE':request.data['Productionreport_delete']
        }
        
        
        PrinterPool_json = {
            'READ': request.data['Printerpool_read'], 
            'CREATE':request.data['Printerpool_create'], 
            'UPDATE': request.data['Printerpool_update'],
            'DELETE':request.data['Printerpool_delete']
        }
        
        Applicationserver_Changepassword_json = {
            'READ': request.data['Applicationserver_Changepassword_read'], 
            'CREATE':request.data['Applicationserver_Changepassword_create'], 
            'UPDATE': request.data['Applicationserver_Changepassword_update'],
            'DELETE':request.data['Applicationserver_Changepassword_delete']
        }
        
        Inspectiondashboard_json = {
            'READ': request.data['Inspectiondashboard_read'], 
              
        }
        Rework_json = {
            'READ': request.data['Rework_read'],
            'CREATE':request.data['Rework_create'],  
            'DELETE':request.data['Rework_delete']
        }
        Applicationserver_History_json = {
            'READ': request.data['Applicationserver_History_read'], 
            'DELETE': request.data['Applicationserver_History_delete'], 
           
        }
        Applicationserver_Backup_json = {
            'READ': request.data['Applicationserver_Backup_read'], 
            'CREATE':request.data['Applicationserver_Backup_create'], 
            'UPDATE': request.data['Applicationserver_Backup_update'],
            'DELETE': request.data['Applicationserver_Backup_delete'],   
        }
        Manualupload_json = {
            'READ': request.data['Manualupload_read'], 
            'CREATE':request.data['Manualupload_create'], 
            'UPDATE': request.data['Manualupload_update'],
            'DELETE': request.data['Manualupload_delete'], 
           
        }
        Applicationserver_reports_json = {
            'READ': request.data['Applicationserver_reports_read'], 
              
        }
        Printerjobs_json = {
            'READ': request.data['Printerjobs_read'], 
            'CREATE':request.data['Printerjobs_create'], 
            'UPDATE': request.data['Printerjobs_update'],
            'DELETE': request.data['Printerjobs_delete'], 
           
        }
        Scannerjobs_json = {
            'READ': request.data['Scannerjobs_read'], 
              
        }
        
        Sapdata_json = {
            'READ': request.data['Sapdata_read'], 
            'CREATE':request.data['Sapdata_create'], 
            'UPDATE': request.data['Sapdata_update'],
            'DELETE': request.data['Sapdata_delete'], 
           
        }
        
        Trash_json = {
            'READ': request.data['Trash_read'], 
            
            'DELETE': request.data['Trash_delete'], 
           
        }
        
        

        
      
        
        if(request.data['userrole']=='admin'):
            userrole = UserrolePermissions.objects.get(activity_name = 'registeredUsers')
            userrole.admin = Registeredusers_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='productionorder')
            userrole.admin=Productionorder_json
            userrole.save()
            
            # userrole=UserrolePermissions.objects.get(activity_name='sendtoshipping')
            # userrole.admin= SendtoShip_json
            # userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='shippingorder')
            userrole.admin=ShippingOrder_json
            userrole.save()
            
            
            userrole=UserrolePermissions.objects.get(activity_name="stock")
            userrole.admin=Stock_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='company')
            userrole.admin=Company_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='customer')
            userrole.admin=Customer_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='customerlocation')
            userrole.admin=CustomerLocation_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='product')
            userrole.admin=Product_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='manufacturinglocation')
            userrole.admin=ManufacturingLocation_json
            userrole.save()
            
            
            userrole=UserrolePermissions.objects.get(activity_name='registeredsystem')
            userrole.admin=RegisteredSystem_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='history')
            userrole.admin=History_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='dashboard')
            userrole.admin=Dashboard_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='snprovider')
            userrole.admin=SnProvider_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name="gtinpool")
            userrole.admin=GtinPool_json
            userrole.save()
            
            
            userrole=UserrolePermissions.objects.get(activity_name="printerpool")
            userrole.admin=PrinterPool_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='auditreport')
            userrole.admin=Auditreport_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='shippingreport')
            userrole.admin=Shippingreport_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='productionreport')
            userrole.admin=Productionreport_json
            userrole.save()
            
            
            userrole=UserrolePermissions.objects.get(activity_name='applicationchangepassword')
            userrole.admin=Applicationserver_Changepassword_json
            userrole.save()
            
            inspectiondashboard = UserrolePermissions.objects.get(activity_name='inspectiondashboard')
            inspectiondashboard.admin = Inspectiondashboard_json
            inspectiondashboard.save() 
            
            rework = UserrolePermissions.objects.get(activity_name='rework')
            rework.admin = Rework_json  
            rework.save()
            
            applicationserverhistory = UserrolePermissions.objects.get(activity_name='applicationserverhistory')
            applicationserverhistory.admin = Applicationserver_History_json
            applicationserverhistory.save()
            
            applicationserverbackup = UserrolePermissions.objects.get(activity_name='applicationserverbackup')
            applicationserverbackup.admin = Applicationserver_Backup_json
            applicationserverbackup.save()
            
            manualupload = UserrolePermissions.objects.get(activity_name='manualupload')
            manualupload.admin =  Manualupload_json 
            manualupload.save()
            
            applicationserverreport = UserrolePermissions.objects.get(activity_name='applicationserverreport')
            applicationserverreport.admin =  Applicationserver_reports_json 
            applicationserverreport.save()
            
            printerjobs = UserrolePermissions.objects.get(activity_name='printerjobs')
            printerjobs.admin =   Printerjobs_json
            printerjobs.save()
            
            scannerjobs = UserrolePermissions.objects.get(activity_name='scannerjobs')
            scannerjobs.admin =  Scannerjobs_json
            scannerjobs.save()
            
            sapdata = UserrolePermissions.objects.get(activity_name='sapdata')
            sapdata.admin = Sapdata_json
            sapdata.save()
            
            trashdata = UserrolePermissions.objects.get(activity_name='trash')
            trashdata.admin = Trash_json
            trashdata.save()
            
            
            
            
            
           
            
            
            return Response(200)
        elif(request.data['userrole']=='masterdata'):
            userrole = UserrolePermissions.objects.get(activity_name = 'registeredUsers')
            userrole.masterdata = Registeredusers_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name= 'productionorder')
            userrole.masterdata= Productionorder_json
            userrole.save()
            
            # userrole=UserrolePermissions.objects.get(activity_name='sendtoshipping')
            # userrole.masterdata= SendtoShip_json
            # userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='shippingorder')
            userrole.masterdata=ShippingOrder_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name="stock")
            userrole.masterdata=Stock_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='company')
            userrole.masterdata=Company_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='customer')
            userrole.masterdata=Customer_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='customerlocation')
            userrole.masterdata=CustomerLocation_json
            userrole.save()
        
            userrole=UserrolePermissions.objects.get(activity_name='product')
            userrole.masterdata=Product_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='manufacturinglocation')
            userrole.masterdata=ManufacturingLocation_json
            userrole.save()
            
            
            userrole=UserrolePermissions.objects.get(activity_name='registeredsystem')
            userrole.masterdata=RegisteredSystem_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='history')
            userrole.masterdata=History_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='dashboard')
            userrole.masterdata=Dashboard_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='snprovider')
            userrole.masterdata=SnProvider_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='gtinpool')
            userrole.masterdata=GtinPool_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='printerpool')
            userrole.masterdata=PrinterPool_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='auditreport')
            userrole.masterdata=Auditreport_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='shippingreport')
            userrole.masterdata=Shippingreport_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='productionreport')
            userrole.masterdata=Productionreport_json
            userrole.save()
            
                        
            userrole=UserrolePermissions.objects.get(activity_name='applicationchangepassword')
            userrole.masterdata=Applicationserver_Changepassword_json
            userrole.save()
            
            inspectiondashboard = UserrolePermissions.objects.get(activity_name='inspectiondashboard')
            inspectiondashboard.masterdata = Inspectiondashboard_json
            inspectiondashboard.save()
            
            rework = UserrolePermissions.objects.get(activity_name='rework')
            rework.masterdata = Rework_json
            rework.save()
            
            applicationserverhistory = UserrolePermissions.objects.get(activity_name='applicationserverhistory')
            applicationserverhistory.masterdata = Applicationserver_History_json
            applicationserverhistory.save()
            
            applicationserverbackup = UserrolePermissions.objects.get(activity_name='applicationserverbackup')
            applicationserverbackup.masterdata = Applicationserver_Backup_json
            applicationserverbackup.save()
            
            manualupload = UserrolePermissions.objects.get(activity_name='manualupload')
            manualupload.masterdata=  Manualupload_json 
            manualupload.save()
            
            applicationserverreport = UserrolePermissions.objects.get(activity_name='applicationserverreport')
            applicationserverreport.masterdata =  Applicationserver_reports_json 
            applicationserverreport.save()
            
            printerjobs = UserrolePermissions.objects.get(activity_name='printerjobs')
            printerjobs.masterdata =   Printerjobs_json
            printerjobs.save()
            
            scannerjobs = UserrolePermissions.objects.get(activity_name='scannerjobs')
            scannerjobs.masterdata = Scannerjobs_json
            scannerjobs.save()
            
            sapdata = UserrolePermissions.objects.get(activity_name='sapdata')
            sapdata.masterdata = Sapdata_json
            sapdata.save()
            
            trashdata = UserrolePermissions.objects.get(activity_name='trash')
            trashdata.masterdata = Trash_json
            trashdata.save()
            
           
            
            
        
        
        
        
        
            
            return Response(200)
        elif(request.data['userrole']=='supervisor'):
            userrole = UserrolePermissions.objects.get(activity_name = 'registeredUsers')
            userrole.supervisor = Registeredusers_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='productionorder')
            userrole.supervisor=Productionorder_json
            userrole.save()
            
            # userrole=UserrolePermissions.objects.get(activity_name='sendtoshipping')
            # userrole.supervisor=SendtoShip_json
            # userrole.save()
            
            
            userrole=UserrolePermissions.objects.get(activity_name='shippingorder')
            userrole.supervisor=ShippingOrder_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='stock')
            userrole.supervisor=Stock_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='company')
            userrole.supervisor=Company_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='customer')
            userrole.supervisor=Customer_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='customerlocation')
            userrole.supervisor=CustomerLocation_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='product')
            userrole.supervisor=Product_json
            userrole.save()
            
            
            userrole=UserrolePermissions.objects.get(activity_name='manufacturinglocation')
            userrole.supervisor=ManufacturingLocation_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='registeredsystem')
            userrole.supervisor=RegisteredSystem_json
            userrole.save()
            
            
            userrole=UserrolePermissions.objects.get(activity_name='history')
            userrole.supervisor=History_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='dashboard')
            userrole.supervisor=Dashboard_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='snprovider')
            userrole.supervisor=SnProvider_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name="gtinpool")
            userrole.supervisor=GtinPool_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name="printerpool")
            userrole.supervisor=PrinterPool_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='auditreport')
            userrole.supervisor=Auditreport_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='shippingreport')
            userrole.supervisor=Shippingreport_json
            userrole.save()
            
            
            userrole=UserrolePermissions.objects.get(activity_name='productionreport')
            userrole.supervisor=Productionreport_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='applicationchangepassword')
            userrole.supervisor=Applicationserver_Changepassword_json
            userrole.save()
            
            inspectiondashboard = UserrolePermissions.objects.get(activity_name='inspectiondashboard')
            inspectiondashboard.supervisor = Inspectiondashboard_json
            inspectiondashboard.save()
            
            rework = UserrolePermissions.objects.get(activity_name='rework')
            rework.supervisor = Rework_json
            rework.save()
            
            applicationserverhistory = UserrolePermissions.objects.get(activity_name='applicationserverhistory')
            applicationserverhistory.supervisor = Applicationserver_History_json
            applicationserverhistory.save()
            
            applicationserverbackup = UserrolePermissions.objects.get(activity_name='applicationserverbackup')
            applicationserverbackup.supervisor = Applicationserver_Backup_json
            applicationserverbackup.save()
            
            manualupload = UserrolePermissions.objects.get(activity_name='manualupload')
            manualupload.supervisor =  Manualupload_json 
            manualupload.save()
            
            applicationserverreport = UserrolePermissions.objects.get(activity_name='applicationserverreport')
            applicationserverreport.supervisor =  Applicationserver_reports_json 
            applicationserverreport.save()
            
            printerjobs = UserrolePermissions.objects.get(activity_name='printerjobs')
            printerjobs.supervisor=   Printerjobs_json
            printerjobs.save()
            
            scannerjobs = UserrolePermissions.objects.get(activity_name='scannerjobs')
            scannerjobs.supervisor =   Scannerjobs_json
            scannerjobs.save()
            
            sapdata = UserrolePermissions.objects.get(activity_name='sapdata')
            sapdata.supervisor =   Sapdata_json
            sapdata.save()
            
            trashdata = UserrolePermissions.objects.get(activity_name='trash')
            trashdata.supervisor = Trash_json
            trashdata.save()
            
            return Response(200)
        elif(request.data['userrole']=='operator'):
            userrole = UserrolePermissions.objects.get(activity_name = 'registeredUsers')
            userrole.operator = Registeredusers_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='productionorder')
            userrole.operator=Productionorder_json
            userrole.save()
            
            # userrole=UserrolePermissions.objects.get(activity_name='sendtoshipping')
            # userrole.operator=SendtoShip_json
            # userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='shippingorder')
            userrole.operator=ShippingOrder_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='stock')
            userrole.operator=Stock_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='company')
            userrole.operator=Company_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='customer')
            userrole.operator=Customer_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='customerlocation')
            userrole.operator=CustomerLocation_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='product')
            userrole.operator=Product_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='manufacturinglocation')
            userrole.operator=ManufacturingLocation_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='registeredsystem')
            userrole.operator=RegisteredSystem_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='history')
            userrole.operator=History_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='dashboard')
            userrole.operator=Dashboard_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='snprovider')
            userrole.operator=SnProvider_json
            userrole.save()
            
            
            userrole=UserrolePermissions.objects.get(activity_name="gtinpool")
            userrole.operator=GtinPool_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name="printerpool")
            userrole.operator=PrinterPool_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='auditreport')
            userrole.operator=Auditreport_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='shippingreport')
            userrole.operator=Shippingreport_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='productionreport')
            userrole.operator=Productionreport_json
            userrole.save()
            
            
            userrole = UserrolePermissions.objects.get(activity_name = 'applicationchangepassword')
            userrole.operator = Applicationserver_Changepassword_json
            userrole.save()
            
            inspectiondashboard = UserrolePermissions.objects.get(activity_name='inspectiondashboard')
            inspectiondashboard.operator = Inspectiondashboard_json
            inspectiondashboard.save()
            
            rework = UserrolePermissions.objects.get(activity_name='rework')
            rework.operator = Rework_json
            rework.save()
            
            applicationserverhistory = UserrolePermissions.objects.get(activity_name='applicationserverhistory')
            applicationserverhistory.operator= Applicationserver_History_json
            applicationserverhistory.save()
            
            applicationserverbackup = UserrolePermissions.objects.get(activity_name='applicationserverbackup')
            applicationserverbackup.operator = Applicationserver_Backup_json
            applicationserverbackup.save()
            
            manualupload = UserrolePermissions.objects.get(activity_name='manualupload')
            manualupload.operator =  Manualupload_json 
            manualupload.save()
            
            applicationserverreport = UserrolePermissions.objects.get(activity_name='applicationserverreport')
            applicationserverreport.operator =  Applicationserver_reports_json 
            applicationserverreport.save()
            
            printerjobs = UserrolePermissions.objects.get(activity_name='printerjobs')
            printerjobs.operator =   Printerjobs_json
            printerjobs.save()
            
            scannerjobs = UserrolePermissions.objects.get(activity_name='scannerjobs')
            scannerjobs.operator =   Scannerjobs_json
            scannerjobs.save()
            
            sapdata = UserrolePermissions.objects.get(activity_name='sapdata')
            sapdata.operator = Sapdata_json
            sapdata.save()
            
            trashdata = UserrolePermissions.objects.get(activity_name='trash')
            trashdata.operator = Trash_json
            trashdata.save()
            
            return Response(200)
      

class UserrolePermissionsRead(APIView):
    def get(self, request):
        detailsObj = UserrolePermissions.objects.all().order_by('id')
        serializeObj = UserrolePermissionsSerializer(detailsObj, many = True)
        return Response(serializeObj.data)
    
# ..............................................................................
# BACKUP DATA CODE 
class TrashHistory(APIView):
    def delete(self, request, pk):
        # name=request.data['Name']
        try:
            detailsObj =History.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = History.objects.all().filter(id=pk)
        detailObj=History.objects.filter(id=pk).update(historyflag=True)
      
       
        historySave = History(modelname='history',
                              savedid=pk,
                              operationdone='deletetotrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Deleted the history by " +  request.data["savedid"] +" to trash")
        historySave.save()
        return Response(200)

class RestoreTrashHistory(APIView):
    def delete(self, request, pk):
        
        try:
            detailsObj = History.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = History.objects.all().filter(id=pk)
        detailObj=History.objects.filter(id=pk).update(historyflag=False)
       
       
        historySave = History(modelname='history',
                              savedid=pk,
                              operationdone='restorefromtrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Restored the history by " + request.data["savedid"] + " from trash")
        historySave.save()
        return Response(200) 
    
class TrashUser(APIView):
    def delete(self, request, pk):
        name=request.data['Name']
        try:
            detailsObj =Register.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = Register.objects.all().filter(id=pk)
        detailObj=Register.objects.filter(id=pk).update(registerflag=True)
      
       
        historySave = History(modelname='register',
                              savedid=pk,
                              operationdone='deletetotrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Deleted the user " +  name +" to trash")
        historySave.save()
        return Response(200)

class RestoreTrashUser(APIView):
    def delete(self, request, pk):
        name=request.data['Name']
        try:
            detailsObj = Register.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = Register.objects.all().filter(id=pk)
        detailObj=Register.objects.filter(id=pk).update(registerflag=False)
       
       
        historySave = History(modelname='register',
                              savedid=pk,
                              operationdone='restorefromtrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Restored the user " + name +" from trash")
        historySave.save()
        return Response(200)
    
    # ....................................................................
class LoginModelView(APIView):
    def get(self, request):
        detailsObj = Loginmodel.objects.all()
        serializeObj = LoginModelSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = LoginModelSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateLoginModel(APIView):
    def put(self, request, pk):
        try:
            detailObj = Loginmodel.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = LoginModelSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)      