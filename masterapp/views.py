from django.shortcuts import render
from rest_framework import generics

from masterapp.models import Company, Customers,BarCodeType,SnProvider,Stock,Locations,ShipPO,Product,ProductionOrder
from masterapp.serializers import CompanySerializer, CustomersSerializer,BarCodeTypeSerializer,SnProviderSerializer,StockSerializer,LocationSerializer,ShipPOSerializer,ProductionOrderSerializer,ProductSerializer,CompanyErpSerializer,ProductPropertySerializer,ShipPOPropertySerializer,ProductionOrderPropertySerializer,CompanyPropertySerializer
# from masterapp.permissions import ObjectDestroyPermission, Productpermission
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from masterapp import serializers
from accounts.models import History
import datetime
# from django_filters.rest_framework import  DjangoFilterBackend
# from apps_extra_code.custom_list_search_filter import CustomSearchFilter



class CompanyView(APIView):
    def get(self, request):
        detailsObj = Company.objects.all()
        serializeObj = CompanySerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = CompanySerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class updateCompany(APIView):
    def put(self, request, pk):
        try:
            detailObj = Company.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = CompanySerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteCompany(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Company.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
class  Companyindividual(APIView):
    def get(self, request, id):
        detailsObj =Company.objects.all().filter(id=id)
        serializeObj = CompanySerializer(detailsObj, many=True)
        return Response(serializeObj.data) 
# ----------------------------------------------------
class CompanyErpView(APIView):
    def get(self, request):
        detailsObj = Company.objects.all()
        serializeObj = CompanyErpSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = CompanyErpSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class updateCompanyErp(APIView):
    def put(self, request, pk):
        try:
            detailObj = Company.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = CompanyErpSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class  CompanyErpindividual(APIView):
    def get(self, request, id):
        detailsObj =Company.objects.all().filter(id=id)
        serializeObj = CompanyErpSerializer(detailsObj, many=True)
        return Response(serializeObj.data) 
    #//////////////////////////////////////////////////////////////


class CompanyPropertyView(APIView):
    def get(self, request):
        detailsObj = Company.objects.all()
        serializeObj = CompanyPropertySerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = CompanyPropertySerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class updateCompanyProperty(APIView):
    def put(self, request, pk):
        try:
            detailObj = Company.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = CompanyPropertySerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class  CompanyPropertyindividual(APIView):
    def get(self, request, id):
        detailsObj =Company.objects.all().filter(id=id)
        serializeObj = CompanyPropertySerializer(detailsObj, many=True)
        return Response(serializeObj.data) 














#customers view
# ______________________________________________


class CustomersView(APIView):
    def get(self, request):
        detailsObj = Customers.objects.all()
        serializeObj = CustomersSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = CustomersSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateCustomer(APIView):
    def put(self, request, pk):
        try:
            detailObj =Customers.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = CustomersSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteCustomer(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Customers.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
    
class CustomerViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = Customers.objects.all().filter(id=id)
        serializeObj = CustomersSerializer(detailsObj, many=True)
        return Response(serializeObj.data)       
#----------------------------------------------------------

class LocationsView(APIView):
    def get(self, request):
        detailsObj = Locations.objects.all()
        serializeObj = LocationSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = LocationSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History( modelName='Location',
                    savedID=device.id,operationDone='create', doneByUser=request.data['loggedInUser'] ,          
                    doneByUserRole=request.data['userrole'],doneDateTime=datetime.datetime.now())
            historysave.save()
            return Response(request.data['loggedInUser'])
            return Response(200)
        return Response(serializeObj.errors)

class updateLocation(APIView):
    def put(self, request, pk):
        try:
            detailObj =Locations.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = LocationSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History(modelName='Locations',
                                savedID=pk,
                                operationDone='update',
                                doneByUser=request.data['loggedInUser'] ,          
                                doneByUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class deleteLocation(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Locations.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
    
class LocationViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = Locations.objects.all().filter(id=id)
        serializeObj = LocationSerializer(detailsObj, many=True)
        return Response(serializeObj.data)    
    
#______________________________________________________________

class ProductPropertyView(APIView):
    def get(self, request):
        detailsObj = Product.objects.all()
        serializeObj = ProductPropertySerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = ProductPropertySerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class updateProductProperty(APIView):
    def put(self, request, pk):
        try:
            detailObj = Product.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ProductPropertySerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)



class deleteProductProperty(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Product.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)

class  ProductindividualProperty(APIView):
    def get(self, request, id):
        detailsObj =Product.objects.all().filter(id=id)
        serializeObj = ProductPropertySerializer(detailsObj, many=True)
        return Response(serializeObj.data) 
#-----------------------------------------------------

class ProductView(APIView):
    def get(self, request):
        detailsObj =Product.objects.all()
        serializeObj = ProductSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj =ProductSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History( modelName='Product',
                    savedID=device.id,operationDone='create', doneByUser=request.data['loggedInUser'] ,          
                    doneByUserRole=request.data['userrole'],doneDateTime=datetime.datetime.now())
            historysave.save()
            return Response(request.data['loggedInUser'])
        return Response(serializeObj.errors)

class updateProduct(APIView):
    def put(self, request, pk):
        try:
            detailObj =Product.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ProductSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()                       
                                
            historysave=History(modelName="Product",
                                savedID=pk,
                                operationDone='update',
                                doneByUser=request.data['loggedInUser'] ,          
                                doneByUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
            
            return Response(request.data['loggedInUser'])
        return Response(serializeObj.errors)

class deleteProduct(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Product.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)

class  Productindividual(APIView):
    def get(self, request, id):
        detailsObj =Product.objects.all().filter(id=id)
        serializeObj = ProductSerializer(detailsObj, many=True)
        return Response(serializeObj.data) 
#---------------------------------------------------------------------------------

class ShipPOView(APIView):
    def get(self, request):
        detailsObj =ShipPO.objects.all()
        serializeObj = ShipPOSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
  
        serializeObj = ShipPOSerializer(data=request.data)

        if serializeObj.is_valid():

            device=serializeObj.save()
            historysave=History( modelName='ShipPO',
                    savedID=device.id,operationDone='create', doneByUser=request.data['loggedInUser'] ,          
                    doneByUserRole=request.data['userrole'],doneDateTime=datetime.datetime.now())
            historysave.save()


           
            
            record = ProductionOrder.objects.get(id=request.data["process_order_number"])
            record.status = "Shipping"
            record.save()
            return Response(request.data['loggedInUser'])
            

        return Response(serializeObj.errors)

            

class updateShipPO(APIView):
    def put(self, request, pk):
        try:
            detailObj =ShipPO.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ShipPOSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History( modelName='ShipPO',
                    savedID=pk,operationDone='update', doneByUser=request.data['loggedInUser'] ,          
                    doneByUserRole=request.data['userrole'],doneDateTime=datetime.datetime.now())
            historysave.save()

            return Response(request.data['loggedInUser'])
        return Response(serializeObj.errors)

class deleteShipPO(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ShipPO.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
class ShippoViewIndividual(APIView):
      def get(self, request, id):
        detailsObj = ShipPO.objects.all().filter(id=id)
        serializeObj = ShipPOSerializer(detailsObj, many=True)
        return Response(serializeObj.data)
    
 #///////////////////////////////////////////////////////////////////   
    
class ShipPoPropertyView(APIView):
    def get(self, request):
        detailsObj = ShipPO.objects.all()
        serializeObj = ShipPOPropertySerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = ShipPOPropertySerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class updateShipPoProperty(APIView):
    def put(self, request, pk):
        try:
            detailObj = ShipPO.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ShipPOPropertySerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)



class deleteShipPoProperty(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ShipPO.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)

class  ShipPoindividualProperty(APIView):
    def get(self, request, id):
        detailsObj =ShipPO.objects.all().filter(id=id)
        serializeObj = ShipPOPropertySerializer(detailsObj, many=True)
        return Response(serializeObj.data)     
#-----------------------------------------------------------------------
class ProductionOrderView(APIView):
    def get(self, request):
        detailsObj =ProductionOrder.objects.all()
        serializeObj = ProductionOrderSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

 
    def post(self, request):
        serializeObj =ProductionOrderSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History( modelName='ProductionOrder',
                    savedID=device.id,operationDone='create', doneByUser=request.data['loggedInUser'] ,          
                    doneByUserRole=request.data['userrole'],doneDateTime=datetime.datetime.now())
            historysave.save()


            return Response(request.data['loggedInUser'])
        return Response(serializeObj.errors)

class ProductionOrderViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = ProductionOrder.objects.all().filter(id=id)
        serializeObj = ProductionOrderSerializer(detailsObj, many=True)
        return Response(serializeObj.data)
class updateProductionOrder(APIView):
    def put(self, request, pk):
        try:
            detailObj =ProductionOrder.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ProductionOrderSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History( modelName='ProductionOrder',
                    savedID=pk,operationDone='update', doneByUser=request.data['loggedInUser'] ,          
                    doneByUserRole=request.data['userrole'],doneDateTime=datetime.datetime.now())
            historysave.save()


            return Response(request.data['loggedInUser'])
        return Response(serializeObj.errors)

class deleteProductionOrder(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ProductionOrder.objects.get(pk=pk)
        except:
            return Response("Not found in database")
    
            detailsObj.delete()
    

    
        return Response(200)
#/////////////////////////////////////////////////////

class PoProperty(APIView):
    def get(self, request):
        detailsObj = ProductionOrder.objects.all()
        serializeObj = ProductionOrderPropertySerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = ProductionOrderPropertySerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class updatePoProperty(APIView):
    def put(self, request, pk):
        try:
            detailObj = ProductionOrder.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ProductionOrderPropertySerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class  PoPropertyindividual(APIView):
    def get(self, request, id):
        detailsObj =ProductionOrder.objects.all().filter(id=id)
        serializeObj = ProductionOrderPropertySerializer(detailsObj, many=True)
        return Response(serializeObj.data) 












#-----------------------------------------------------------------

class BarCodeTypeView(APIView):
    def get(self, request):
        detailsObj =BarCodeType.objects.all()
        serializeObj = BarCodeTypeSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

  
    def post(self, request):
        serializeObj =BarCodeTypeSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History(modelName="BarCodeType",
                                savedID=device.id,
                                operationDone='create',
                                doneByUser=request.data['loggedInUser'],          
                                doneByUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
                            
            return Response(request.data['loggedInUser'])
        return Response(serializeObj.errors)

class updateBarcodetype(APIView):
    def put(self,request,pk):
        try:
            detailObj =BarCodeType.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = BarCodeTypeSerializer(detailObj,data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History(modelName="BarCodeType",
                                savedID=pk,
                                operationDone='update',
                                doneByUser=request.data['loggedInUser'] ,          
                                doneByUserRole=request.data['userrole'],
                                doneDateTime=datetime.datetime.now())
            historysave.save()
            
            return Response(request.data['loggedInUser'])
        return Response(serializeObj.errors)

class deleteBarcodetype(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = BarCodeType.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
    
    
class  Barcodeindividual(APIView):
    def get(self, request, id):
        detailsObj =BarCodeType.objects.all().filter(id=id)
        serializeObj = BarCodeTypeSerializer(detailsObj, many=True)
        return Response(serializeObj.data)     
    #-----------------------------------------------------------------

class SnproviderView(APIView):
    def get(self, request):
        detailsObj =SnProvider.objects.all()
        serializeObj = SnProviderSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj =SnProviderSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateSnprovider(APIView):
    def put(self, request, pk):
        try:
            detailObj=SnProvider.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = SnProviderSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteSnprovider(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = SnProvider.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
#-------------------------------------------------------------
class StockView(APIView):
    def get(self, request):
        detailsObj =Stock.objects.all()
        serializeObj = StockSerializer(detailsObj, many = True)
        return Response(serializeObj.data)
  
   


  
    def post(self, request):
        serializeObj =StockSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateStock(APIView):
    def put(self,request,pk):
        try:
            detailObj =Stock.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = StockSerializer(detailObj,data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteStock(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Stock.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)

class Stockclosedview(APIView):
       def get(self, request):
            detailsObj = ProductionOrder.objects.all().filter(status='Closed')
            serializeObj = ProductionOrderSerializer(detailsObj, many=True)
          
            
            return Response(serializeObj.data)      