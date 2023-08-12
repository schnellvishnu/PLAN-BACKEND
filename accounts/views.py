from django.shortcuts import render
from rest_framework import generics

from accounts.models import  UserRole,AuditLog,Register,History,UserrolePermissions,UserAuditHistoryOnly
from accounts.serializers import UserRoleSerializer,HistorySerializer,RegisterSerializer,UserrolePermissionsSerializer,UserHistorySerializer
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
        
        
        PrinterPool_json = {
            'READ': request.data['Printerpool_read'], 
            'CREATE':request.data['Printerpool_create'], 
            'UPDATE': request.data['Printerpool_update'],
            'DELETE':request.data['Printerpool_delete']
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
            
            userrole=UserrolePermissions.objects.get(activity_name="printrpool")
            userrole.operator=PrinterPool_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='auditreport')
            userrole.operator=Auditreport_json
            userrole.save()
            
            userrole=UserrolePermissions.objects.get(activity_name='shippingreport')
            userrole.operator=Shippingreport_json
            userrole.save()
            
            
            return Response(200)
      

class UserrolePermissionsRead(APIView):
    def get(self, request):
        detailsObj = UserrolePermissions.objects.all().order_by('id')
        serializeObj = UserrolePermissionsSerializer(detailsObj, many = True)
        return Response(serializeObj.data)
    
