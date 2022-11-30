from django.shortcuts import render
from rest_framework import generics

from masterapp.models import Company, Customers,BarCodeType,SnProvider,Stock,Locations,ShipPO,Product,ProductionOrder
from masterapp.serializers import CompanySerializer, CustomersSerializer,BarCodeTypeSerializer,SnProviderSerializer,StockSerializer,LocationSerializer,ShipPOSerializer,ProductionOrderSerializer,ProductSerializer
# from masterapp.permissions import ObjectDestroyPermission, Productpermission
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from masterapp import serializers
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
# ----------------------------------------------------
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
#----------------------------------------------------------

class LocationsView(APIView):
    def get(self, request):
        detailsObj = Locations.objects.all()
        serializeObj = LocationSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = LocationSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
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
#______________________________________________________________

class ProductView(APIView):
    def get(self, request):
        detailsObj =Product.objects.all()
        serializeObj = ProductSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj =ProductSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
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
            return Response(200)
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
#-----------------------------------------------------

class ShipPOView(APIView):
    def get(self, request):
        detailsObj =ShipPO.objects.all()
        serializeObj = ShipPOSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj =ShipPOSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
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
            return Response(200)
        return Response(serializeObj.errors)

class deleteShipPO(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ShipPO.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
#-----------------------------------------------------------------------
class ProductionOrderView(APIView):
    def get(self, request):
        detailsObj =ProductionOrder.objects.all()
        serializeObj = ProductionOrderSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

 
    def post(self, request):
        serializeObj =ProductionOrderSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
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
            return Response(200)
        return Response(serializeObj.errors)

class deleteProductionOrder(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ProductionOrder.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)


#-----------------------------------------------------------------
class BarCodeTypeView(APIView):
    def get(self, request):
        detailsObj =BarCodeType.objects.all()
        serializeObj = BarCodeTypeSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

  
    def post(self, request):
        serializeObj =BarCodeTypeSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
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
            return Response(200)
        return Response(serializeObj.errors)

class deleteBarcodetype(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = BarCodeType.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
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