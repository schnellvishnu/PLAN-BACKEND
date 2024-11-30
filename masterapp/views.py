from django.shortcuts import render
from rest_framework import generics

from masterapp.models import Company, Customers,BarCodeType,SnProvider,Stock,Locations,ShipPO,Product,ProductionOrder,Markets,Gtins,PrinterdataTable,Downloadcodes,ProdReport,Allocatednumbers
from masterapp.serializers import CompanySerializer, CustomersSerializer,BarCodeTypeSerializer,SnProviderSerializer,StockSerializer,LocationSerializer,ShipPOSerializer,ProductionOrderSerializer,ProductSerializer,CompanyErpSerializer,ProductPropertySerializer,ShipPOPropertySerializer,ProductionOrderPropertySerializer,CompanyPropertySerializer,CompanyTracelinkSerializer,LocationPropertySerializer,ProductErpSerializer ,MarketsSerializer,CustomerTracelinkSerializer,ProductHrSerializer,ProductMarketpageSerializer,ProductionorderHrfSerializer,GtinsSerializer,PrinterSerializer,DownloadcodesSerializer,CustomersPropertySerializer,BalancedslnoSerializer,ProdReportSerializer,AllocatednumberSerializer
# from masterapp.permissions import ObjectDestroyPermission, Productpermission
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from masterapp import serializers
from accounts.models import History
import datetime
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User
# from django_filters.rest_framework import  DjangoFilterBackend
# from apps_extra_code.custom_list_search_filter import CustomSearchFilter
from django.http import JsonResponse
import json
import ftplib
import csv
from collections import defaultdict
from itertools import chain
from csv import DictWriter
from collections import Counter
import pandas as pd
import os
import pandas as pd
import os
from pathlib import Path
from zipfile import ZipFile
from xml.dom import minidom
# import lxml.etree
# import lxml.builder    
import xml.etree.ElementTree as ET
# frag_xml_tree = ET.parse("xmlfiles/commissioning.xml")

import http.client
import urllib.parse
import xml.dom.minidom
import re


class CompanyView(APIView):
    def get(self, request):
        detailsObj = Company.objects.all().order_by('id')
        serializeObj = CompanySerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = CompanySerializer(data=request.data)
       
        if serializeObj.is_valid():
            serializeObj.save()
            device=serializeObj.save()
            historysave=History( modelname='Company',
                    savedid=device.id,
                    operationdone='create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Created A New Company"+request.data["company_name"]+"\t"+"by"+"\t"+ request.data['loggedInUsername'],
                    donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(request.data['loggedInUsername'])
            
            
            
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
            historysave=History(modelname='Company',
                                savedid=pk,
                                operationdone='update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyemployeeid=request.data['loggedInemployeeid'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Company  of id" + request.data["uniqueid"] + "\t"+"Updated",
                                donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteCompany(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Company.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        uniqueid=str(request.data['id'])
        historysave=History(modelname='Company',
                                savedid=pk,
                                operationdone='delete',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Company  of id" + uniqueid + "\t"+"Deleted",
                                donedatetime=datetime.datetime.now())
        historysave.save()

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
            device=serializeObj.save()
            historysave=History( modelname='Company',
                    savedid=device.id,
                    operationdone='erp of this id created',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Company Erp of id"+device.id+"\t"+"Created",
                    donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(request.data['loggedInUsername'])
            
            
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
            historysave=History(modelname='Company',
                                savedid=pk,
                                operationdone='erp of this id update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Company Erp of id" + str(request.data["uniqueid"]) + "\t"+"Updated",
                                donedatetime=datetime.datetime.now())
            historysave.save()
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
            device=serializeObj.save()
            historysave=History( modelname='Company',
                    savedid=device.id,
                    operationdone='property of this id create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Company Property of id" + request.data["uniqueid"] + "\t"+"Created",
                    donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(request.data['loggedInUsername'])
            
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
            historysave=History(modelname='Company',
                                savedid=pk,
                                operationdone='property of this id update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Company Property of id" + request.data["uniqueid"] + "\t"+"Updated",
                                donedatetime=datetime.datetime.now())
            historysave.save()
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
        detailsObj = Customers.objects.all().order_by('-id')
        serializeObj = CustomersSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = CustomersSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History(modelname='Customer',
                    savedid=device.id,
                    operationdone='create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Created A New Customer"+request.data["name"]+"\t"+"by"+"\t"+ request.data['loggedInUsername'],
                    donedatetime=datetime.datetime.now())
            historysave.save()


            return Response(request.data['loggedInUsername'])
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
            historysave=History(modelname='Customer',
                                savedid=pk,
                                operationdone='update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Customer of id"+"\t"+request.data["uniqueid"]+"\t"+"Updated", 
                                donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteCustomer(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Customers.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        
        uniqueid=str(request.data['id'])
        # print(uniqueid)
        historysave=History(modelname='Customer',
                                savedid=pk,
                                operationdone='Delete',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Customer of id"+"\t"+uniqueid+"\t"+"Deleted",  
                                donedatetime=datetime.datetime.now())
        historysave.save()
        detailsObj.delete()
        return Response(200)
    
class CustomerViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = Customers.objects.all().filter(id=id)
        serializeObj = CustomersSerializer(detailsObj, many=True)
        return Response(serializeObj.data) 

class CustomernameViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = Customers.objects.all().filter(name=id)
        serializeObj = CustomersSerializer(detailsObj, many=True)
        return Response(serializeObj.data)    
    
class CustomersTracelinkView(APIView):
        def get(self, request):
            detailsObj = Customers.objects.all()
            serializeObj = CustomerTracelinkSerializer(detailsObj, many = True)
            return Response(serializeObj.data)

   
        def post(self, request):
            serializeObj = CustomerTracelinkSerializer(data=request.data)
            if serializeObj.is_valid():
                serializeObj.save()
                return Response(200)
            return Response(serializeObj.errors)

class updateCustomerTracelink(APIView):
    def put(self, request, pk):
        try:
            detailObj =Customers.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = CustomerTracelinkSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History(modelname='Customer',
                                savedid=pk,
                                operationdone='Customer Tracelink of this id Update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Customer Tracelink of id"+"\t"+request.data["uniqueid"]+"\t"+"Updated",  
                                donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)


    
class CustomerTracelinkViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = Customers.objects.all().filter(id=id)
        serializeObj = CustomerTracelinkSerializer(detailsObj, many=True)
        return Response(serializeObj.data) 
        
class CustomerPropertyview(APIView):
        def get(self, request):
            detailsObj = Customers.objects.all()
            serializeObj = CustomersPropertySerializer(detailsObj, many = True)
            return Response(serializeObj.data)
        
        def post(self, request):
            serializeObj = CustomersPropertySerializer(data=request.data)
            if serializeObj.is_valid():
                device=serializeObj.save()
                historysave=History( modelname='Customer',
                    savedid=device.id,
                    operationdone='Customer Property create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Customer Property of id"+"\t"+request.data["uniqueid"]+"\t"+"Updated",  
                    donedatetime=datetime.datetime.now())
                historysave.save()
                return Response(request.data['loggedInUsername'])
                return Response(200)
            return Response(serializeObj.errors)
        
class updateCustomerProperty(APIView):
    def put(self, request, pk):
        try:
            detailObj = Customers.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = CustomersPropertySerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History(modelname='Customer',
                                savedid=pk,
                                operationdone='Customer property of this id update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Customer Property of id"+"\t"+request.data["uniqueid"]+"\t"+"Updated",   
                                donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)


class CustomerPropertyViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = Customers.objects.all().filter(id=id)
        serializeObj = CustomersPropertySerializer(detailsObj, many=True)
        return Response(serializeObj.data)     
        
    
          
#---------------------------------------------------------------------------

class LocationsView(APIView):
    def get(self, request):
        detailsObj = Locations.objects.all().order_by('id')
        serializeObj = LocationSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = LocationSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History( modelname='Location',
                    savedid=device.id,
                    operationdone='create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Created A New Customer Location"+request.data["name"]+"\t"+"by"+"\t"+ request.data['loggedInUsername'],
                    donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(request.data['loggedInUsername'])
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
            uniqueid=str(request.data["uniqueid"])
            
            historysave=History(modelname='Locations',
                                savedid=pk,
                                operationdone='Update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Customer Location of id "+ uniqueid +" Updated",   
                                donedatetime=datetime.datetime.now())
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
        uniqueid=str(request.data['id'])
        historysave=History(modelname='Locations',
                                savedid=pk,
                                operationdone='update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Customer Location of id"+"\t"+uniqueid+"\t"+"Deleted",   
                                donedatetime=datetime.datetime.now())
        historysave.save()
        return Response(200)
    
class LocationViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = Locations.objects.all().filter(id=id)
        serializeObj = LocationSerializer(detailsObj, many=True)
        return Response(serializeObj.data)    
    
#______________________________________________________________
class LocationPropertyview(APIView):
        def get(self, request):
            detailsObj = Locations.objects.all()
            serializeObj = LocationPropertySerializer(detailsObj, many = True)
            return Response(serializeObj.data)
        
        def post(self, request):
            serializeObj = LocationPropertySerializer(data=request.data)
            if serializeObj.is_valid():
                device=serializeObj.save()
                historysave=History( modelname='Location',
                    savedid=device.id,
                    operationdone='Location Property create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="hi",
                    donedatetime=datetime.datetime.now())
                historysave.save()
                return Response(request.data['loggedInUsername'])
                return Response(200)
            return Response(serializeObj.errors)
        
class updateLocationProperty(APIView):
    def put(self, request, pk):
        try:
            detailObj = Locations.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = LocationPropertySerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History(modelname='Locations',
                                savedid=pk,
                                operationdone=' Location property of this id update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Customer Location Property of id"+"\t"+request.data["uniqueid"]+"\t"+"Updated",    
                                donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)


class LocationPropertyViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = Locations.objects.all().filter(id=id)
        serializeObj = LocationPropertySerializer(detailsObj, many=True)
        return Response(serializeObj.data)     
#//////////////////////////////////////////////////////////////////////////////////////    

class ProductPropertyView(APIView):
    def get(self, request):
        detailsObj = Product.objects.all()
        serializeObj = ProductPropertySerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = ProductPropertySerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History(modelname='Product',
                    savedid=device.id,
                    operationdone='property of this id create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="hi",
                    donedatetime=datetime.datetime.now())
            historysave.save() 
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
            historysave=History(modelname="Product",
                                savedid=pk,
                                operationdone='property of this id update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Product Property of id"+"\t"+request.data["uniqueid"]+"\t"+"Updated",     
                                donedatetime=datetime.datetime.now())
            
            historysave.save()
            
            return Response(request.data['loggedInUsername'])
            return Response(200)
        return Response(serializeObj.errors)



class deleteProductProperty(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Product.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        historysave=History(modelname="Product",
                                savedid=pk,
                                operationdone='property of this id delete',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'], 
                                donedatetime=datetime.datetime.now())
        
        historysave.save()
        return Response(200)

class  ProductindividualProperty(APIView):
    def get(self, request, id):
        detailsObj =Product.objects.all().filter(id=id)
        serializeObj = ProductPropertySerializer(detailsObj, many=True)
        return Response(serializeObj.data) 
    
    
class ProducthrfView(APIView):
    def get(self, request):
        detailsObj = Product.objects.all()
        serializeObj = ProductHrSerializer(detailsObj, many = True)
        return Response(serializeObj.data)
    

   
    def post(self, request):
        serializeObj = ProductHrSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History(modelname='Product',
                    savedid=device.id,
                    operationdone='Hrf  of this id create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="hi",
                    donedatetime=datetime.datetime.now())
            historysave.save()
            
            return Response(200)
        return Response(serializeObj.errors)

class updateProducthr(APIView):
    def put(self, request, pk):
        try:
            detailObj = Product.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ProductHrSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            historysave=History(modelname="Product",
                                savedid=pk,
                                operationdone='Hrf of this id update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Product Hrf of id"+"\t"+request.data["uniqueid"]+"\t"+"Updated",      
                                donedatetime=datetime.datetime.now())
            
            historysave.save()
            
            return Response(request.data['loggedInUsername'])
            return Response(200)
        return Response(serializeObj.errors)





class  Productindividualhrf(APIView):
    def get(self, request, id):
        detailsObj =Product.objects.all().filter(id=id)
        serializeObj = ProductHrSerializer(detailsObj, many=True)
        return Response(serializeObj.data)     
#-----------------------------------------------------

class ProductView(APIView):
    def get(self, request):
        detailsObj =Product.objects.all().order_by('-id')
        serializeObj = ProductSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
   
    def post(self, request):
        serializeObj = ProductSerializer(data=request.data)
        
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History(modelname='Product',
                    savedid=device.id,
                    operationdone='create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Created A New Product" +"\t"+request.data["name"]+"\t"+"by"+"\t"+ request.data['loggedInUsername'],
                    donedatetime=datetime.datetime.now())
            historysave.save()
            # record = Product.objects.get(request.data["status"]==True)
            # record.status = "Confirmed" 
            # record.save()
            return Response(request.data['loggedInUsername'])
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
                                
            historysave=History(modelname="Product",
                                savedid=pk,
                                operationdone='Update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Product  of id"+"\t"+request.data["uniqueid"]+"\t"+"Updated",      
                                donedatetime=datetime.datetime.now())
            
            historysave.save()
            
            return Response(request.data['loggedInUsername'])
        return Response(serializeObj.errors)

class deleteProduct(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Product.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        uniqueid=str(request.data['id'])
        historysave=History(modelname="Product",
                                savedid=pk,
                                operationdone='delete',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Product  of id"+"\t"+ uniqueid+"\t"+"Deleted",       
                                donedatetime=datetime.datetime.now())
        
        historysave.save()
        return Response(200)

class  Productindividual(APIView):
    def get(self, request, id):
        detailsObj =Product.objects.all().filter(id=id)
        serializeObj = ProductSerializer(detailsObj, many=True)
        return Response(serializeObj.data) 
    
    
# class Hrfjsonview(APIView):    
#     def get(self,request):
#               data=list(Product.objects.values())
#               serializeObj = ProducthrfSerializer(data, many=False)
#               return JsonResponse(serializeObj.data,safe=False)
     
     
     
#     def post(self, request):
#         serializeObj = ProducthrfSerializer(data=request.data)
#         if serializeObj.is_valid():
#             serializeObj.save()
            
#             return Response(200)
#         return JsonResponse(serializeObj.data,safe=False)
    
# class updateProducthrf(APIView):
#     def put(self, request, pk):
#         try:
#             detailObj =Product.objects.get(pk=pk)
#         except:
#             return Response("Not found in database")

#         serializeObj = ProducthrfSerializer(detailObj, data=request.data)
#         if serializeObj.is_valid():
#             serializeObj.save()                       
                                
            # historysave=History(modelName="Product",
            #                     savedID=pk,
            #                     operationDone='update',
            #                     doneByUser=request.data['loggedInUser'] ,          
            #                     doneByUserRole=request.data['userrole'],
            #                     doneDateTime=datetime.datetime.now())
            # historysave.save()
            
        #     return Response(200)
        # return JsonResponse(serializeObj.data,safe=False) 
        
          
#---------------------------------------------------------------------------------
class ProductErpview(APIView):
    def get(self,request):
         detailobj=Product.objects.all()
         serializeobj=ProductErpSerializer(detailobj,many=True)
         return Response(serializeobj.data)
     
    def post(self,request):
            serializeobj=ProductErpSerializer(data=request.data)
            
            if serializeobj.is_valid():
                device=serializeobj.save()
                
                historysave=History(modelname='Product',
                savedid=device.id,
                operationdone='erp of this id created',
                donebyuser=request.data['loggedInUsername'],
                donebyuserrole=request.data['loggedInUserrole'], 
                description="hi",
                donedatetime=datetime.datetime.now())
                historysave.save()
                return Response(200)
            return Response(serializeobj.errors)
 
 
class UpdateProductErp(APIView):
    def put(self,request,pk):
        try:
            detailobj=Product.objects.get(pk=pk)
        except:
            return Response("Not found")
        serializeobj=ProductErpSerializer(detailobj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            historysave=History(modelname="Product",
                                savedid=pk,
                                operationdone='erp of this id updated',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Product  of id"+"\t"+request.data["uniqueid"]+"\t"+"ErP Updated",       
                                donedatetime=datetime.datetime.now())
            
            historysave.save()
            
            return Response(request.data['loggedInUsername'])
            return Response(200)
        return Response(serializeobj.errors) 
    
class ProductErpIndividual(APIView):
    def get(self,request,id):
        detailobj=Product.objects.all().filter(id=id)
        serializeobj=ProductErpSerializer(detailobj,many= True)
        return Response(serializeobj.data)                               
                            


class ProductMarketview(APIView):
    def get(self,request):
         detailobj=Product.objects.all()
         serializeobj=ProductMarketpageSerializer(detailobj,many=True)
         return Response(serializeobj.data)
     
    def post(self,request):
            serializeobj= ProductMarketpageSerializer(data=request.data)
            if serializeobj.is_valid():
                serializeobj.save()
                return Response(200)
            return Response(serializeobj.errors)
 
 
class UpdateProductmarket(APIView):
    def put(self,request,pk):
        try:
            detailobj=Product.objects.get(pk=pk)
            
        except:
            return Response("Not found")
        serializeobj=ProductMarketpageSerializer(detailobj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors) 
    
class ProductmarketIndividual(APIView):
    def get(self,request,id):
        detailobj=Product.objects.all().filter(id=id)
        serializeobj=ProductMarketpageSerializer(detailobj,many= True)
        return Response(serializeobj.data)                               
                            

                                
                            

    
             
class ShipPOView(APIView):
    def get(self, request):
        detailsObj =ShipPO.objects.all().order_by('-id')
        serializeObj = ShipPOSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

    def post(self, request):
  
        serializeObj = ShipPOSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            record = ProductionOrder.objects.get(id=request.data["process_order_number"])
            record.status = "Shipping"
            record.save()
            # productionorder_num=request.data['process_no_original'] 
            # record = ProductionOrder.objects.get(process_order_number=productionorder_num)
            # record.status = "Shipping"
            # record.save()
            if request.method == 'POST': 
                productionorder_num=request.data['process_no_original'] 
                stockObj = Stock.objects.all().filter( process_order_number=productionorder_num)
                stockObj.delete()
            historysave=History( modelname='ShipPO',
                   savedid=device.id,
                    operationdone='create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Created A New Shiipingorder"+request.data["shipping_order_name"]+"\t"+"by"+"\t"+ request.data['loggedInUsername'],
                    donedatetime=datetime.datetime.now())
            historysave.save() 
            # record = ProductionOrder.objects.get(id=request.data["process_order_number"])
            # record.status = "Shipping"
            # record.save()
            return Response(request.data['process_no_original']) 
        return Response(serializeObj.errors)

            

class updateShipPO(APIView):
    def put(self, request, pk):
        # print(request.data["uniqueid"])
        # uniqueid=str(request.data["uniqueid"])
        # print(uniqueid)
        # print(request.data["shipping_order_name"])
        # print(request.data["process_order_number"])
        # print(request.data["destination_location"])
        # print(request.data["source_location"])
        # print(request.data["subject_name"])
        # print(request.data["shipping_date"])
        # print(request.data["shipping_time"])
        # print(request.data["process_no_original"])
        # print(request.data["status"])
        try:
            detailObj =ShipPO.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ShipPOSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            # historysave=History(modelname="ShippingOrder",
            #                     savedid=pk,
            #                     operationdone='Updated',
            #                     donebyuser=request.data['loggedInUsername'],
            #                     donebyuserrole=request.data['loggedInUserrole'],
            #                     description="ShippingOrder  of id"+"\t"+uniqueid+"\t"+"Updated",       
            #                     donedatetime=datetime.datetime.now())
            
            # historysave.save()

            return Response(request.data['loggedInUsername'])
        return Response(serializeObj.errors)

class deleteShipPO(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ShipPO.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        uniqueid=str(request.data['id'])
        historysave=History( modelname='ShippingOrder',
                    savedid=pk,operationdone='delete', 
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'],
                    description="ShippingOrder  of id"+"\t"+uniqueid+"\t"+"Delete",       
                    donedatetime=datetime.datetime.now())
        historysave.save()
        return Response(200)
class ShippoViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = ShipPO.objects.all().filter(id=id)
        serializeObj = ShipPOSerializer(detailsObj, many=True)
        return Response(serializeObj.data)

    
class ShippoProductionordernumberGetingIndividual(APIView):
    def get(self,request,id):
     
           
           
            detailsObj=ShipPO.objects.all().filter(process_no_original=id)
            if detailsObj:
                serializeObj=ShipPOSerializer(detailsObj,many=True)
                return Response(serializeObj.data)  
            else:
                return Response(100)
       
class ShipPOViewget(APIView):
    def get(self, request):
        detailsObj =ShipPO.objects.all()
        serializeObj = ShipPOSerializer(detailsObj, many = True)
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
            device=serializeObj.save()
             
            historysave=History( modelname='ShipPO',
                   savedid=device.id,
                    operationdone='Property of this id create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="hi",
                    donedatetime=datetime.datetime.now())
            historysave.save()
            
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
            
            historysave=History(modelname="ShipPO",
                                savedid=pk,
                                operationdone='proiperty of this id updated',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'], 
                                donedatetime=datetime.datetime.now())
            
            historysave.save()
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
    
    
# class  ShipPoReportindividualProperty(APIView):
#     def get(self, request, id):
#         detailsObj =ShipPO.objects.all().filter(process_no_original=id)
#         serializeObj = ShipPOPropertySerializer(detailsObj, many=True)
#         return Response(serializeObj.data) 
        
#................................................................... 
class ShippoAuditReportdate(APIView):  
    def get(self, request):
        detailsObj = ShipPO.objects.all()
        serializeObj =ShipPOSerializer(detailsObj, many=True)
        # fromDate = request.data["datefrom"]
        # toDate = request.data["dateto"]
        # response  = ProductionReport.objects.filter( production_date=fromDate, production_date__lte=toDate)
        return Response(200)
    
    def post(self, request):
        serializeObj = ShipPOSerializer(data=request.data)
        v=[]
        startdate = request.data["datefrom"]
        
        toDate = request.data["dateto"]
        # fromDate=str(request.POST.get('datefrom'))
        # toDate=str(request.POST.get("dateto"))
        # response  =ProductionReport.objects.all().filter(production_date=id)
        
        response  =ShipPO.objects.all().filter(shipping_date__range=(startdate, toDate))
        serializeObj = ShipPOSerializer(response , many=True)
        return Response(serializeObj.data)
        
#-----------------------------------------------------------------------
class ProductionOrderView(APIView):
    def get(self, request):
        detailsObj =ProductionOrder.objects.all().order_by('id').reverse()
        serializeObj = ProductionOrderSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

 
    def post(self, request):
        serializeObj =ProductionOrderSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History(modelname='ProductionOrder',
                    savedid=device.id,
                    operationdone='create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Created A New Productionorder"+request.data["process_order_number"]+"\t"+"by"+"\t"+ request.data['loggedInUsername'],
                    donedatetime=datetime.datetime.now())
            historysave.save()


            return Response(request.data['loggedInUsername'])
        return Response(serializeObj.errors)

class ProductionOrderViewIndividual(APIView):
    def get(self, request, id):
        detailsObj = ProductionOrder.objects.all().filter(id=id)
        serializeObj = ProductionOrderSerializer(detailsObj, many=True)
        return Response(serializeObj.data)
class ProductionOrderReportIndividual(APIView):
    def get(self, request, id):
        detailsObj = ProductionOrder.objects.all().filter(batch_number=id)
        serializeObj = ProductionOrderSerializer(detailsObj, many=True)
        return Response(serializeObj.data)
    #ippol uiiiuiiooppmh
class ProductionOrdernumberusingprintertableIndividual(APIView):
      def get(self, request, id):
        detailsObj = ProductionOrder.objects.all().filter(process_order_number=id)
        if detailsObj:
            serializeObj = ProductionOrderSerializer(detailsObj, many=True)
            return Response(serializeObj.data)
        
        else:
            return Response(100)
       

  
class updateProductionOrder(APIView):
    def put(self, request, pk):
        try:
            detailObj =ProductionOrder.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ProductionOrderSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
           
            if request.data['status']=='Closed':
                stocksave=Stock(process_order_number =request.data['process_order_number'],
                                             product_conn=request.data['product_conn'],
                                             batch_number =request.data['batch_number'], 
                                             created_by=request.data['created_by'])
           
                stocksave.save()
                historysave=History(modelname='ProductionOrder',
                                savedid=pk,
                                operationdone='Updated',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'], 
                                donedatetime=datetime.datetime.now())
            
                historysave.save()
            return Response(request.data['loggedInUsername'])
        return Response(serializeObj.errors)

class deleteProductionOrder(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ProductionOrder.objects.get(pk=pk)
        except:
            return Response("Not found in database")
    
        detailsObj.delete()
        historySave = History(modelname='ProductionOrder',
                              savedid=pk,
                              operationdone='delete',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now())
        
        historySave.save()
    
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
            device=serializeObj.save()
            historysave=History(modelname='ProductionOrder',
                savedid=device.id,
                operationdone='Property of this id create',
                donebyuser=request.data['loggedInUsername'],
                donebyuserrole=request.data['loggedInUserrole'], 
                    # description="hi",
                description="Productionorder Property of id"+device.id+"\t"+"Created",
                donedatetime=datetime.datetime.now())
            historysave.save()


            return Response(request.data['loggedInUsername'])
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
            
            historysave=History(modelname='ProductionOrder',
                                savedid=pk,
                                operationdone='Property of this id Updated',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Productionorder Property of id" + "\t" + request.data["uniqueid"]   + "\t"+"Updated", 
                                donedatetime=datetime.datetime.now())
            
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)

class  PoPropertyindividual(APIView):
    def get(self, request, id):
        detailsObj =ProductionOrder.objects.all().filter(id=id)
        serializeObj = ProductionOrderPropertySerializer(detailsObj, many=True)
        return Response(serializeObj.data) 





class ProductionorderhrfView(APIView):
    def get(self, request):
        detailsObj = ProductionOrder.objects.all()
        serializeObj = ProductionorderHrfSerializer(detailsObj, many = True)
        return JsonResponse(serializeObj.data,safe=False)
    

   
    def post(self, request):
        serializeObj = ProductionorderHrfSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History(modelname='ProductionOrder',
                    savedid=device.id,
                    operationdone='Hrf  of this id create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="hi",
                    donedatetime=datetime.datetime.now())
            historysave.save()
            
            return Response(200)
        return JsonResponse(serializeObj.errors,safe=False)

class updateProductionorderhrfView(APIView):
   
    def put(self, request, pk):
        lname=request.data['loggedInUsername']
        try:
            detailObj = ProductionOrder.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ProductionorderHrfSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            print(request.data['loggedInUsername'])
            historysave=History(modelname="ProductionOrder",
                                savedid=pk,
                                operationdone='Hrf of this id update',
                                donebyuser=lname,
                                donebyuserrole=request.data['loggedInUserrole'], 
                                description="Productionorder Hrf of id" + "\t" + request.data["uniqueid"]   + "\t"+"Updated", 
                                donedatetime=datetime.datetime.now())
            
            historysave.save()
            
            # return Response(request.data['loggedInUsername'])
            return Response(200)
        return JsonResponse(serializeObj.errors,safe=False)





class  Productionorderindividualhrf(APIView):
    def get(self, request, id):
        detailsObj =ProductionOrder.objects.all().filter(id=id)
        serializeObj = ProductionorderHrfSerializer(detailsObj, many=True)
        return JsonResponse(serializeObj.data,safe=False)     






#-----------------------------------------------------------------

class BarCodeTypeView(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        
        detailsObj =BarCodeType.objects.all()
        serializeObj = BarCodeTypeSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

  
    def post(self, request):
        serializeObj =BarCodeTypeSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History(modelName="BarCodeType",
                    savedid=device.id,
                    operationdone='create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="hi",
                    donedatetime=datetime.datetime.now())
            historysave.save()
                            
            return Response(request.data['loggedInUsername'])
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

# class deleteBarcodetype(APIView):
#     def delete(self, request, pk):
#         try:
#             detailsObj = BarCodeType.objects.get(pk=pk)
#         except:
#             return Response("Not found in database")

#         detailsObj.delete()
#         return Response(200)
class deleteBarcodetype(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            detailsObj = BarCodeType.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()

        ##### Section to save history
        historySave = History(modelName='BarCodeType',
                              savedID=pk,
                              operationDone='delete',
                              doneByUser=request.data['loggedInUser'],
                              doneByUserRole=request.data['userRole'],
                              doneDateTime=datetime.datetime.now())
        historySave.save()

        return Response(200)


class  Barcodeindividual(APIView):
    def get(self, request, id):
        detailsObj =BarCodeType.objects.all().filter(id=id)
        serializeObj = BarCodeTypeSerializer(detailsObj, many=True)
        return Response(serializeObj.data)     
#-----------------------------------------------------------------

class SnproviderView(APIView):
    def get(self, request):
        detailsObj =SnProvider.objects.all().order_by('-id')
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
    def delete(self, request,pk):
        try:
            detailsObj = SnProvider.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
#-------------------------------------------------------------
class StockView(APIView):
    def get(self, request):
        detailsObj =Stock.objects.all().order_by('-id')
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
#/////////////////////////////////////////////////////////////////////////////////////////
        
        
class Tracelinkview(APIView):
        def get(self,request):
            detailsObj =Company.objects.all()
            serializeObj=CompanyTracelinkSerializer(detailsObj,many=True)
            return Response(serializeObj.data)                    
        
        def post(self,request): 
            serializeObj=CompanyTracelinkSerializer(data=request.data)
            if serializeObj.is_valid():
                  serializeObj.save()
                  return Response(200)
            return Response(serializeObj.errors)
        
class updateTracelink(APIView):
    def put(self,request,pk):
        try:
            detailObj =Company.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = CompanyTracelinkSerializer(detailObj,data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)         
class Tracelinkviewindividual(APIView):
    def get(self,request,id):
        detailsObj =Company.objects.all().filter(id=id)
        serializeObj=CompanyTracelinkSerializer(detailsObj,many=True)
        return Response(serializeObj.data)                    
               
    
# class Erpview(APIView):
#     def get(self,request):
#         detailobj=  Erpsetting.objects.all()
#         serializeobj=ErpSerializer(detailobj,many=True)
#         return Response(serializeobj.data)
    
#     def post(self,request):
#             serializeobj=ErpSerializer(data=request.data)
#             if serializeobj.is_valid():
#                       serializeobj.save()
#                       return Response(200)
#             return Response(serializeobj.errors)
# class updateErpview(APIView):
#     def put(self,request,pk):
#         try:
#             detailObj =Erpsetting.objects.get(pk=pk)
#         except:
#             return Response("Not found in database")

#         serializeObj = ErpSerializer(detailObj,data=request.data)
#         if serializeObj.is_valid():
#             serializeObj.save()
#             return Response(200)
#         return Response(serializeObj.errors)
        
class Marketsview(APIView):
    def get(self,request):
        detailobj= Markets.objects.all()
        serializeobj=MarketsSerializer(detailobj,many=True)
        return Response(serializeobj.data)
    def post(self,request):
        serializeobj=MarketsSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors) 
          
class deleteMarket(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Markets.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)                               
        

# class Gtinview(APIView) :
#         def get(self,request):
#             detailObj=Gtins.objects.all()
#             serializeobj=GtinsSerializer(detailObj,many=True)
#             return Response(serializeobj.data)
        
#         def post(self,request):
#             serializeobj=GtinsSerializer(data=request.data)
#             if serializeobj.is_valid():
#                 serializeobj.save()
#                 return Response(200)
#             return Response(serializeobj.errors) 
        
# class updateGtinview(APIView):
#     def put(self,request,pk):
#         try:
#             detailObj=Gtins.objects.get(pk=pk)
#         except:
#             return Response("Not found in database") 
             
#         serializerobj=GtinsSerializer(detailObj,request.data) 
#         if serializerobj.is_valid():
#             serializerobj.save()
#             return Response(200)
#         return Response(serializerobj.errors) 
        
        
# class deleteGtinview(APIView) :
#     def delete(self,request,pk):
#         try:
#             detailObj=Gtins.objects.get(pk)
#         except:
#             return Response("Not found in database") 
#         detailObj.delete()
#         return Response(200)
    
# class Gtinindividualview(APIView) :
#     def get(self,request,id):
#         detailobj=Gtins.objects.all().filter(id=id)
#         serializeobj=GtinsSerializer(detailobj,many=True)
#         return Response(serializeobj.data)


class Gtinview(APIView) :
        def get(self,request):
            detailObj=Gtins.objects.all().order_by('-id')
            serializeobj=GtinsSerializer(detailObj,many=True)
            return Response(serializeobj.data)
        
        
        
        # def post(self,request):
        #     serializeobj=GtinsSerializer(data=request.data)
            
        #     if serializeobj.is_valid():
        #         device=serializeobj.save()
        #         path = '/SerialNumbers'

        #         filename = 'serial numbers CSV file.csv'




        #         ftp = ftplib.FTP("aplusintellitech.com")

        #         ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        #         ftp.cwd(path)

        #         ftp.retrbinary("RETR " + filename, open("D:/csv_file.csv", 'wb').write)

        #         ftp.quit()




        #         with open("D:/csv_file.csv") as file:

        #             csvreader = csv.reader(file)

        #             for row in csvreader:

        #                 print(row)
                        
        #         gtin=request.data['gtin']
        #         with open("D:/csv_file.csv") as file:
                   

        #             csvreader = csv.reader(file)
        #             array=file.readlines()
                    
        #             array = [row.strip() for row in array]
        #             # print(array[0])
                
        #             # for temp in array:
        #             #     v=temp
        #             #     g=v[18:27]
        #             #     i=0
        #             row_list = ["SN", "Gtin", "Serial no","Status"],
                    
                        
        #                 # i=i+1
              
        #             with open("csvfiles/"+gtin+".csv", 'a', newline='') as file:
                                      
        #                     writer = csv.writer(file)
        #                     writer.writerows(row_list)
        #                     i=0
        #             for temp in array:
        #                     v=temp
        #                     g=v[18:27]
                                    
                          
        #                     valuelist = [i,gtin,g, "notallow"],
                       
                      
                        
        #                     i=i+1
              
        #                     with open("csvfiles/"+gtin+".csv", 'a', newline='') as file:
                                      
        #                         writer = csv.writer(file)
                                
        #                         writer.writerows(valuelist)   
                
        #             # gtin=request.data['gtin']
        #             minq=request.data['minimum_quantity']
              
                
        #             with open("csvfiles/"+gtin+".csv", newline='') as f:
        #                 readobj=csv.reader(f)
        #                 for row in readobj:
        #                     t=row[2]                    
                       
                       
        #             row_list = ["SN", "Gtin", "Serial no","Status","Sending Status"],
                    
                        
        #                 # i=i+1
              
        #             with open("Allocatedcsv/"+gtin+".csv", 'a', newline='') as file:
                                      
        #                     writer = csv.writer(file)
        #                     writer.writerows(row_list)
        #                     i=0
        #                     k=1
        #             with open("csvfiles/"+gtin+".csv", newline='') as f:
        #                     readobj=csv.reader(f)
        #                     for row in readobj:
        #                         t=row[2]        
                          
        #                         valuelist = [i,gtin,t, "allow",minq],
                       
                      
                        
        #                         i=i+1
        #                         k=k+1
        #                         if(k>int(minq)):
        #                             break
                                                
              
        #                         with open("Allocatedcsv/"+gtin+".csv", 'a', newline='') as file:
                                      
        #                             writer = csv.writer(file)
                                    
        #                             writer.writerows(valuelist)
                           
                               
                                
                                
        #             results = pd.read_csv('serialpoolgtin.csv')
        #             count=len(results)
        #             obj = Gtins.objects.get(pk=device.id)
        #             detailObj=Gtins.objects.all().update(snnumbers=count)
                    
                                
                                
        #         return Response(200)
        #     return Response(serializeobj.errors)
        
        
        def post(self,request):
            serializeobj=GtinsSerializer(data=request.data)
            gtin=request.data['gtin']
            
            if serializeobj.is_valid():
                device=serializeobj.save()
                
                path = '/SerialNumbers'
                

                filename = gtin+".csv"




                ftp = ftplib.FTP("aplusintellitech.com")

                ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

                ftp.cwd(path)

                ftp.retrbinary("RETR " + filename, open("D:/csv_file.csv", 'wb').write)

                ftp.quit()




                with open("D:/csv_file.csv") as file:

                    csvreader = csv.reader(file)

                    for row in csvreader:

                        print(row)
                        
              
                with open("D:/csv_file.csv") as file:
                   

                    csvreader = csv.reader(file)
                    array=file.readlines()
                    
                    array = [row.strip() for row in array]
                    i=0
                    # print(array[0])
                
                    # for temp in array:
                    #     v=temp
                    #     g=v[18:27]
                    #     i=0
                    row_list = ["SN", "Gtin", "Serialno","Status"],
                    
                        
                        # i=i+1
              
                    with open("csvfiles/"+gtin+".csv", 'a', newline='') as file:
                                      
                            writer = csv.writer(file)
                            writer.writerows(row_list)
                            # i=0
                    for temp in array:
                            v=temp
                            g=v[18:27]
                                    
                          
                          
                       
                      
                        
                          
              
                            with open("csvfiles/"+gtin+".csv", 'a', newline='') as file:
                                      
                                writer = csv.writer(file)
                                if(i!=0):
                                    valuelist = [i,gtin,g,"notallow"],
                                    writer.writerows(valuelist)
                                i=i+1   
                
                    # gtin=request.data['gtin']
                    # minq=request.data['minimum_quantity']
              
                
                    with open("csvfiles/"+gtin+".csv", newline='') as f:
                        readobj=csv.reader(f)
                        for row in readobj:
                            t=row[2]                    
                       
                       
                    # row_list = ["SN", "Gtin", "Serial no","Status","Sending Status"],
                    
                        
                    #     # i=i+1
              
                    # with open("Allocatedcsv/"+gtin+".csv", 'a', newline='') as file:
                                      
                    #         writer = csv.writer(file)
                    #         writer.writerows(row_list)
                    #         i=0
                    #         k=0
                    # with open("csvfiles/"+gtin+".csv", newline='') as f:
                    #         readobj=csv.reader(f)
                    #         for row in readobj:
                    #             t=row[2]        
                          
                               
                       
                      
                        
                    #             i=i+1
                    #             # k=k+1
                    #             if(k>int(minq)):
                    #                 break
                                                
              
                #                 with open("Allocatedcsv/"+gtin+".csv", 'a', newline='') as file:
                                      
                #                     writer = csv.writer(file)
                #                     if(k!=0):
                #                         valuelist = [i,gtin,t, "allow",minq],
                #                         writer.writerows(valuelist)
                #                     k=k+1
                #                     slnolist=[]
                #                     rowIndex=[]
                #                     counter=1
                #                     loopcounter=-1
                #     with open("csvfiles/"+gtin+".csv", newline='') as f:

                #         readobj=csv.reader(f)

                #         for row in readobj:

                #             if(row[3]=="notallow"):

                #                 slnolist.append(row[2])

                #                 rowIndex.append(loopcounter)

                #                 counter=counter+1

                #             if(counter > int(minq)):

                #                 break

                       

                #             loopcounter=loopcounter+1

                #     json_numbers = json.dumps(slnolist)

                #     df=pd.read_csv("csvfiles/"+gtin+".csv")

                #     for value in rowIndex:

                #         df.loc[value,'Status']="allocated"

                #     df.to_csv("csvfiles/"+gtin+".csv",index=False)
                     
                     
                #     df=pd.read_csv("csvfiles/"+gtin+".csv")
                #     with open("csvfiles/"+gtin+".csv")  as f:
                #             readobj=csv.reader(f)
                #             counter=-1
                #             for row in readobj:
                #                     if counter<int(minq):
                #                         df=df.loc[df['Status']=='notallow']
                #                         df.shape 
                #                     counter=counter+1
                #     df.to_csv("csvfiles/"+gtin+".csv",index=False)                
                                                          
                                                        
                                              
                           
                               
                                
                                
                # gtin=request.data['gtin']
                with open("csvfiles/"+gtin+".csv")  as f:
                    results = pd.read_csv("csvfiles/"+gtin+".csv")
                    count=len(results)
                #     obj = Gtins.objects.get(pk=device.id)
                #     detailObj=Gtins.objects.all().filter(pk=device.id).update(snnumbers=count)
                    
                                
                    obj = Gtins.objects.get(gtin=gtin)
                    detailObj=Gtins.objects.all().filter(gtin=obj.gtin).update(available_quantity=count)                
                return Response(200)
            return Response(serializeobj.errors)
        
        
        
        
        
        


# class updateGtinview(APIView):
#         def put(self,request,pk):
#             try:
#                 detailObj=Gtins.objects.get(pk=pk)
#             except:
#                  return Response("Not found in database") 
             
#             serializerobj=GtinsSerializer(detailObj,request.data) 
#             if serializerobj.is_valid():
#                 device=serializerobj.save()
#                 gtin=request.data['gtin']
#                 minq=request.data['minimum_quantity']
#                 file="csvfiles/"+gtin+".csv"
#                 if(os.path.exists(file) and os.path.isfile(file)):
#                     os.remove(file)
#                     print("file deleted")
#                 else:
#                     print("file not found") 
                
#                 with open("D:/serial numbers CSV file.csv") as file:
                   

#                     csvreader = csv.reader(file)
#                     array=file.readlines()
#                     products_list = list() 
#                     status=list()  
#                     # print(array)
#                     array = [row.strip() for row in array]
#                     # print(array[0])
                
#                     # for temp in array:
#                     #     v=temp
#                     #     g=v[18:27]
#                     #     i=0
                  
#                     row_list = ["SN", "Gtin", "Serial no","Status","Sending Status"],
                    
                        
#                         # i=i+1
              
#                     with open("csvfiles/"+gtin+".csv", 'a', newline='') as file:
                                      
#                             writer = csv.writer(file)
#                             writer.writerows(row_list)
#                             i=1
#                             k=1
#                     for temp in array:
                                            
#                             v=temp
#                             g=v[18:27]        
                          
#                             valuelist = [i,gtin,g, "notallow",minq],
                       
                      
                        
#                             i=i+1
#                             k=k+1
#                             if(k>int(minq)):
#                                 break
                                                
              
#                             with open("csvfiles/"+gtin+".csv", 'a', newline='') as file:
                                   
#                                 writer = csv.writer(file)
#                                 writer.writerows(valuelist)
                                
                                
#                     results = pd.read_csv('serialpoolgtin.csv')
#                     count=len(results)
#                     obj = Gtins.objects.get(pk=device.id)
#                     detailObj=Gtins.objects.all().update(snnumbers=count)
                    
                                
                                
#                 return Response(200)
#             return Response(serializerobj.errors)
class updateGtinview(APIView):
        def put(self,request,pk):
            try:
                detailObj=Gtins.objects.get(pk=pk)
            except:
                 return Response("Not found in database") 
             
            serializerobj=GtinsSerializer(detailObj,request.data)
            gtin=request.data['gtin'] 
            if serializerobj.is_valid():
                serializerobj.save()
                path = '/SerialNumbers'
                

                filename = gtin+".csv"




                ftp = ftplib.FTP("aplusintellitech.com")

                ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

                ftp.cwd(path)

                ftp.retrbinary("RETR " + filename, open("D:/csv_file.csv", 'wb').write)

                ftp.quit()




                with open("D:/csv_file.csv") as file:

                    csvreader = csv.reader(file)

                    for row in csvreader:

                        print(row)
                        
              
                with open("D:/csv_file.csv") as file:
                   

                    csvreader = csv.reader(file)
                    array=file.readlines()
                    
                    array = [row.strip() for row in array]
                    i=0
                    # print(array[0])
                
                    # for temp in array:
                    #     v=temp
                    #     g=v[18:27]
                    #     i=0
                    row_list = ["SN", "Gtin", "Serialno","Status"],
                    
                        
                        # i=i+1
              
                    with open("csvfiles/"+gtin+".csv", 'a', newline='') as file:
                                      
                            writer = csv.writer(file)
                            # writer.writerows(row_list)
                            # i=0
                    for temp in array:
                            v=temp
                            g=v[18:27]
                                    
                          
                          
                       
                      
                        
                          
              
                            with open("csvfiles/"+gtin+".csv", 'a', newline='') as file:
                                      
                                writer = csv.writer(file)
                                if(i!=0):
                                    valuelist = [i,gtin,g,"notallow"],
                                    writer.writerows(valuelist)
                                i=i+1   
                
                    # gtin=request.data['gtin']
                    # minq=request.data['minimum_quantity']
              
                
                    with open("csvfiles/"+gtin+".csv", newline='') as f:
                        readobj=csv.reader(f)
                        for row in readobj:
                            t=row[2]  
                                
                with open("csvfiles/"+gtin+".csv")  as f:
                    results = pd.read_csv("csvfiles/"+gtin+".csv")
                    count=len(results)
                #     obj = Gtins.objects.get(pk=device.id)
                #     detailObj=Gtins.objects.all().filter(pk=device.id).update(snnumbers=count)
                    
                                
                    obj = Gtins.objects.get(gtin=gtin)
                    detailObj=Gtins.objects.all().filter(gtin=obj.gtin).update(available_quantity=count)                
                return Response(200)
            return Response(serializerobj.errors)        
        
class deleteGtinview(APIView) :
    def delete(self,request,pk):
        try:
            detailObj=Gtins.objects.get(pk=pk)
        except:
            return Response("Not found in database") 
        detailObj.delete()
        return Response(200)
    
class Gtinindividualview(APIView) :
        def get(self,request,id):
                detailobj=Gtins.objects.all().filter(id=id)
                serializeobj=GtinsSerializer(detailobj,many=True)
                return Response(serializeobj.data)
class Gtinrcbview(APIView) :
    def get(self,request,id):
                detailobj=Gtins.objects.all().filter(gtin=id)
                serializeobj=GtinsSerializer(detailobj,many=True)
                return Response(serializeobj.data)
                                
                                
class printerview(APIView) :
        def get(self,request):
            detailObj=PrinterdataTable.objects.all().order_by('-id')
            serializeobj=PrinterSerializer(detailObj,many=True)
            return Response(serializeobj.data)
        
        
        
        def post(self,request):
            
            jsonArray=[]
            
          
            gtin=request.data["gtin"]
            type=request.data["type"]
            lot=request.data["lot"]
            print(lot)
            productionorderno=request.data['processordernumber']
            # printerid=request.data['id']
            print(productionorderno)
            try:
                with open("Allocatedcsv/"+lot+".csv", newline='') as f:
                    readobj=csv.reader(f)
                    for row in readobj:
                       if(row[3]=="allocated"):
                            jsonArray.append(row[2])
                            
                        
                    jsonString = json.dumps(jsonArray)
                    # print(jsonString[0:10])
                    childjson= json.loads(jsonString)
                    s1=json.dumps(childjson[0:10])
            except:
                return Response(500)        
            # detailsObj =PrinterdataTable.objects.get(id=productionorderno)
            prodObj=ProductionOrder.objects.get(process_order_number=productionorderno)
            
            
            hrf=prodObj.hrf
            hrfjson=json.loads(hrf)
            print(hrfjson)
            if(type=="type1" or type=="type5"):
                if(hrfjson == None  ):
                    print("jjkhnaffd")                    
                    return Response(400) 
                else:     
                    hrf1=hrfjson["hrf1"]
                    print(hrf1)
                    hrf2=hrfjson["hrf2"]
                    hrf3=hrfjson["hrf3"]
                    hrf4=hrfjson["hrf4"]
                    hrf5=hrfjson["hrf5"]
                    hrf6=hrfjson["hrf6"]
                    hrf1value=hrfjson["hrf1value"]
                    hrf2value=hrfjson["hrf2value"]
                    hrf3value=hrfjson["hrf3value"]
                    hrf4value=hrfjson["hrf4value"]
                    hrf5value=hrfjson["hrf5value"]
                    hrf6value=hrfjson["hrf6value"]
            serializeobj=PrinterSerializer(data=request.data)
                
                                         
            if(type=="type1" or type=="type5"):
                                    
              
                if(hrf1 !="" and hrf1value != ""):  
                                      
                    if serializeobj.is_valid():
                        device=serializeobj.save()
                        obj = PrinterdataTable.objects.get(pk=device.id)
                        detailObj=PrinterdataTable.objects.filter(pk=device.id).update(numbers=jsonString,hrf=hrf) 
                        detailsObj1 =ProductionOrder.objects.get(process_order_number=productionorderno)
                        Obj=ProductionOrder.objects.filter(process_order_number=detailsObj1.process_order_number).update(status="Inproduction") 
                                            
               
                else:  
                                   
                    return Response(400)                         
            else:
                if serializeobj.is_valid():
                    device=serializeobj.save()
                    obj = PrinterdataTable.objects.get(pk=device.id)
                    detailObj=PrinterdataTable.objects.filter(pk=device.id).update(numbers=jsonString,hrf=hrf)
                    
                    detailsObj1 =ProductionOrder.objects.get(process_order_number=productionorderno)
                    Obj=ProductionOrder.objects.filter(process_order_number=detailsObj1.process_order_number).update(status="Inproduction")  
                                        
                return Response(serializeobj.errors) 
            return Response(serializeobj.errors) 
                     
               
           
        
class updatePrinterview(APIView):
        def put(self,request,pk):
            try:
                detailObj=PrinterdataTable.objects.get(pk=pk)
            except:
                 return Response("Not found in database") 
             
            # serializerobj=PrinterSerializer(detailObj,request.data) 
            # if serializerobj.is_valid():
            #      serializerobj.save()
            #      return Response(200)
            # return Response(serializerobj.errors)
            jsonArray=[]
            
          
            gtin=request.data["gtin"]
        
            with open("Allocatedcsv/"+gtin+".csv", newline='') as f:
                readobj=csv.reader(f)
                for row in readobj:
                    
                        jsonArray.append(row[2])
                        # print(row[2])
                    
                jsonString = json.dumps(jsonArray)
                # print(jsonString)
                
                
                
                
            
            # serializeobj=PrinterSerializer(data=request.data)
            # if serializeobj.is_valid():
            #     print("hi")                    
            #     device=serializeobj.save()
            # obj = PrinterdataTable.objects.get(pk=device.id)
            obj = PrinterdataTable.objects.get(id=pk)
            detailObj=PrinterdataTable.objects.filter(pk=pk).update(numbers=jsonString) 
            # print(obj.numbers)  
            return Response(200)
        
        
        
        
        
        
class deletePrinterview(APIView) :
    def delete(self,request,pk):
        try:
            detailObj=PrinterdataTable.objects.get(pk=pk)
        except:
            return Response("Not found in database") 
        detailObj.delete()
        return Response(200)
    
class Printerindividualview(APIView):
        def get(self,request,id):
                detailobj=PrinterdataTable.objects.all().filter(id=id)
                serializeobj=PrinterSerializer(detailobj,many=True)
                return Response(serializeobj.data)        
                                          
class Hrfdata(APIView):
    def get(self,request,id):
        detailsObj = ProductionOrder.objects.get(id=id)
        # print(detailsObj.product_conn)
        prodObj=Product.objects.get(name=detailsObj.product_conn)
        # print(prodObj.hrf4)
        hrfdict={
            "hrf1":prodObj.hrf1,"hrf2":prodObj.hrf2,"hrf3":prodObj.hrf3,"hrf4":prodObj.hrf4,
            "hrf5":prodObj.hrf5,"hrf6":prodObj.hrf6
        }
        jsondata=json.dumps(hrfdict)
        # print(jsondata)
        return Response(jsondata)                                     


class Downloadcodesget(APIView):        
    def get(self,request):
        # detailObj=Downloadcodes.objects.all()
        detailObj=Downloadcodes.objects.all()
        serializeobj=DownloadcodesSerializer(detailObj,many=True)
        return Response(serializeobj.data)
        
        
        
    def post(self,request):
            
        jsonArray=[]
            
          
        # gtin=request.data["gtin"]
        lot=request.data["batch_number"]
        print(lot)
        try:
            with open("Allocatedcsv/"+lot+".csv", newline='') as f:
                    readobj=csv.reader(f)
                    for row in readobj:
                        
                        jsonArray.append(str(row[1])+str(row[2]))
                        
                    jsonString = json.dumps(jsonArray)
                    print(jsonString)
        except:
            return Response(300)    
        serializeobj=DownloadcodesSerializer(data=request.data)
        if serializeobj.is_valid():
            device=serializeobj.save()
            obj = Downloadcodes.objects.get(pk=device.id)
            
            detailObj=Downloadcodes.objects.filter(pk=device.id).update(serialnumberwithgtin=jsonString)
        detailsObj5 = ProductionOrder.objects.get(batch_number=lot)
        Obj=ProductionOrder.objects.filter(batch_number=detailsObj5.batch_number).update(btncontrollstatus="Downloaded") 
                
        return Response(serializeobj.errors)
    
class Downloadindividualview(APIView):
    def get(self,request,id):
        detailobj=Downloadcodes.objects.all().filter(process_order_number=id)
        serializeobj=DownloadcodesSerializer(detailobj,many=True)
        return Response(serializeobj.data)                                                           
                 
                 
                 
class Xmldataindividual(APIView):
    # def get(self, request,id):
    #     # detailsObj = Shipmentfiledata.objects.get(id=id)
    #     # print(detailsObj.product_conn)
    #     # prodObj=Company.objects.get(company_name=detailsObj.filesendernumber)
    #     # hrfdict={
    #     #     "hrf1":prodObj.hrf1
    #     # }                  
    #     detailObj=Shipmentfiledata.objects.all()
    #     serializeobj=ShipmentdataSerializer(detailObj,many=True)
        # return Response(serializeobj.data)
        # tree=ET.parse("xmlfiles/commissioning.xml")
        
        # ET.register_namespace("","urn:tracelink:mapper:sl:serial_number_exchange")
        # # frag_xml_tree.write("xmlfiles/commissioning.xml")
        # root=tree.getroot()
        
    def post(self,request):
                            
        processordernumber=request.data["process_no_original"]  

        try:
            filereceivernumber=request.data["filereceivernumber"]
        except:
            return Response(50)                                
        # serializeobj=ShipmentdataSerializer(data=request.data)
        try:
            filesenderno=request.data["filesendernumber"]
        except:
            return Response(100) 
        
        try:
             businessname2=request.data["business_name2"]
        except:
            return Response(150)
        try:
             to_business_part_lookupid1=request.data["to_business_part_lookupid1"]
        except:
            return Response(250)
        
        try:
             lot_number=request.data["lot_number"]
        except:
            return Response(300)
        try:
            filedate=request.data["filedate"]
        except:
            return Response(350)
        try:
           filetime=request.data["filetime"]
        except:
              return Response(400)
        
        try:
             business_name=request.data["business_name"]

        except:
              return Response(450)
        
        try:
               postalcode=request.data["postalcode"]
        except:
              return Response(500)
        try:
              country=request.data["country"]
        except:
              return Response(550)
        try:
             street1=request.data["street1"]
        except:
              return Response(600)  
        try:
             State_or_region=request.data["State_or_region"]
        except:
            return Response(650)
        try:
            city=request.data["city"]
        except:
            return Response(700)
        try:
            deliverynumber=request.data["deliverynumber"]
        except:
            return Response(300)
        try:
             transactionidentifier2=request.data["transactionidentifier2"]
        except:     
            return Response(300)
        try:
            factilty_type1=request.data["factilty_type1"]
        except:
              return Response(750)
        try:
            business_id_type=request.data["business_id_type"]
        
        except:
            return Response(50) 
        try:
            filecontrolnumber=request.data["filecontrolnumber"]
        except:
             return Response(800)
        try: 
            delivery_completeflag=request.data["delivery_completeflag"]
        except:
            return Response(850)
        try:
            transactiondate=request.data["transactiondate"]
        except:
            return Response(900)
        try:
             
            transactiontime=request.data["transactiontime"]
        except:
            return Response(950)
        try:
             salesdistribution_type=request.data["salesdistribution_type"]
        except:
            return Response(1000)
        try:
              shipfrom_countrycode=request.data["shipfrom_countrycode"]
        except:
            return Response(1050)
        try:
             shipto_countrycode=request.data["shipto_countrycode"]
        except:
            return Response(1070)
        detailobj=Locations.objects.get(id=filesenderno)
        # print(detailobj.name)
        
       
       
       
      
        
     
        transactionidentifier=request.data["transactionidentifier"]
       
  
       
        
        try:
        # internal_material_code=request.data["internal_material_code"]
            detailsObj1=ProductionOrder.objects.get(process_order_number= processordernumber)

            internal_material_code=detailsObj1.internal_material_number
        except:
            return Response(3000)
        # print("imc") 
        # print(internal_material_code)
        
        # quantity=request.data["quantity"]
        try:
            detailsObjquantity=ProductionOrder.objects.get(process_order_number= processordernumber)
            quantity=detailsObjquantity.quantity
            
        except:
            return Response(3050)
       
       
       
        
     
      
        
        
        try:
            detailobfactilty_type1=Customers.objects.get(id=factilty_type1)
            detailobfa1=Customers.objects.get(name=detailobfactilty_type1)
            factilty_type1value=detailobfa1.siteid
            # print(factilty_type1value)
        except:
            return Response(4000)
            
        # factilty_type2=request.data["factilty_type2"]
        try:

            detailobfa2=Customers.objects.get(name=detailobfactilty_type1)
            factilty_type2value=detailobfa2.company_gln
        except:
            return Response(4050)
            
        # business_name2=request.data["business_name2"]
       
        
        detailobjb2=Locations.objects.get(id=businessname2)
        
     
        
       
       
       
        
       
       
       
       
        
        # street2=request.data["street2"]
        try:

            detailobjstreet2=Locations.objects.get(name=detailobjb2)
            street2=detailobjstreet2.address
        except:
            return Response(5000)
        # city2=request.data["city2"]
        try:

            detailobjcity2=Locations.objects.get(name=detailobjb2)
            city2= detailobjcity2.city
        except:
            return Response(5050)   
        
        # State_or_region2=request.data["State_or_region"]
        try:
            detailobjState_or_region2=Locations.objects.get(name=detailobjb2)
            State_or_region2=detailobjState_or_region2.state
        except:
            return Response(6000)
        
        # postalcode2=request.data["postalcode2"]
        try:
                
            detailobjpostalcode2=Locations.objects.get(name=detailobjb2)
            postalcode2=detailobjpostalcode2.zip
        except:
            return Response(6050)
            
        # detailobjb2.name
        # district=request.data["district"]
        try:
            detailobjdistrict=Locations.objects.get(name=detailobjb2)
            district=detailobjdistrict.district
        except:
            return Response(7000)
            
        # country2=request.data["country2"]
        try:
            detailobjcountry2=Locations.objects.get(name=detailobjb2)
            country2=detailobjcountry2.country
        except:
            return Response(7050)
       
        try:
            detailobjto_business_part_lookupid1=Locations.objects.get(id=to_business_part_lookupid1)
            s1=detailobjto_business_part_lookupid1.customer_id 
            # detailobjbusiness_part_lookupid1=Locations.objects.get(name=detailobjto_business_part_lookupid1)
            
            to_business=Customers.objects.get(name=s1)
            
            to_business_part_lookupid=to_business.tobusinessparylookupid
        except:
            return Response(8000)
        # print(to_business.tobusinessparylookupid)
        
        
        
        
        
        # to_shiptolocationlookupid=request.data["to_shiptolocationlookupid"]
        try:
            detailobjshiptolocationlookupid=Locations.objects.get(name=detailobjb2)
            to_shiptolocationlookupid=detailobjshiptolocationlookupid.ship_to_locationlookup_id
        except:
            return Response(8050)
             
        # print(filesenderno)
        # if serializeobj.is_valid():
        #     device=serializeobj.save()
            
        # detailObj=Shipmentfiledata.objects.get(pk=device.id)
        root = ET.Element("som:SOMSalesShipmentMessage")
        root.set(r"xmlns:xsi",r"http://www.w3.org/2001/XMLSchema-instance")
        root.set(r"xmlns:cmn",r"urn:tracelink:mapper:sl:commontypes")
        root.set(r"xmlns:som",r"urn:tracelink:mapper:sl:serialized_operations_manager")
        root.set(r"xmlns",r"urn:tracelink:mapper:sl:serialized_operations_manager")
        
        ET.dump(root)
        # ,attrib={'xsi:schemaLocation':'urn:tracelink:mapper:sl:serial_number_exchange C:\Users\lucy\Documents\TRACEL~1\PRODUC~1\SERIAL~1\SOMGRS~1\TL_XML_SerialNumberDispositionAssigned_2_0.xsd', 'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance" xmlns:cmn:"urn:tracelink:mapper:sl:commontypes','xmlns:cmn':'urn:tracelink:mapper:sl:commontypes','xmlns':'urn:tracelink:mapper:sl:serial_number_exchange" xmlns:snx="urn:tracelink:mapper:sl:serial_number_exchange','xmlns:snx':'urn:tracelink:mapper:sl:serial_number_exchange'}
        a1 = ET.Element("som:ControlFileHeader")
        root.append(a1)
        ab1 =ET.SubElement(a1, "cmn:FileSenderNumber")
        ab1.text = str(detailobj.name)
        ab2 = ET.SubElement(a1, "cmn:FileReceiverNumber")
        ab2.text = str(filereceivernumber)
        ab3 = ET.SubElement(a1, "cmn:FileControlNumber")
        ab3.text =str(filecontrolnumber)
        ab4 = ET.SubElement(a1, "cmn:FileDate")
        ab4.text = str(filedate)
        ab5 = ET.SubElement(a1, "cmn:FileTime")
        ab5.text = str(filetime)
        a2 = ET.Element("som:MessageBody")
        root.append(a2)
        ab3=ET.SubElement(a2,"cmn:DeliveryNumber")
        ab3.text = str(deliverynumber)
        ab4=ET.SubElement(a2,"cmn:DeliveryCompleteFlag")
        ab4.text =str(delivery_completeflag)
        ab2 = ET.SubElement(a2, "som:OrderDetails")
        ########################## iNSIDE LOOP
    
        abc2 = ET.SubElement(ab2, "cmn:TransactionIdentifier", attrib={'type':'PO'})
        abc2.text=str(transactionidentifier)
        abcd2 = ET.SubElement(ab2, "cmn:TransactionIdentifier", attrib={'type':'ASN'})
        abcd2.text =str(transactionidentifier2)
        abcd3 = ET.SubElement(ab2, "cmn:TransactionDate")
        abcd3.text = str(transactiondate)
        abcd4 = ET.SubElement(ab2, "cmn:TransactionTime")
        abcd4.text = str(transactiontime)
        abcd5 = ET.SubElement(ab2, "cmn:ShipFromCountryCode")
        abcd5.text = str(shipfrom_countrycode)
        abcd6 = ET.SubElement(ab2, "cmn:ShipToCountryCode")
        abcd6.text = str(shipto_countrycode)
        abcd7 = ET.SubElement(ab2, "cmn:SalesDistributionType")
        abcd7.text = str(salesdistribution_type)
        abcd8 = ET.SubElement(ab2, "cmn:OrderItemList")
        abcd9 = ET.SubElement(abcd8, "cmn:OrderItem")
        abcd10 = ET.SubElement(abcd9, "cmn:InternalMaterialCode")
        abcd10.text = str(internal_material_code)
        abcd11 = ET.SubElement(abcd9, "cmn:LotNumber")
        abcd11.text = str(lot_number)
        abcd12 = ET.SubElement(abcd9, "cmn:Quantity")
        abcd12.text = str(quantity)
        abcd13 = ET.SubElement(ab2,"cmn:SenderInfo")
        abcd14 = ET.SubElement(abcd13, "cmn:FromBusinessPartyInfo")
        abcd15 = ET.SubElement(abcd14, "cmn:BusinessId", attrib={'type':'GLN'})
        abcd15.text = str(business_id_type)
        abcd16 = ET.SubElement(abcd14,"cmn:BusinessInfo")
        abcd17 = ET.SubElement(abcd16, "cmn:BusinessName")
        abcd17.text = str(business_name)
        abcd18 = ET.SubElement(abcd16, "cmn:Street1")
        abcd18.text = str(street1)
        
        abcd19 = ET.SubElement(abcd16, "cmn:City")
        abcd19.text = str(city)
        abcd20 = ET.SubElement(abcd16, "cmn:StateOrRegion")
        abcd20.text = str(State_or_region)
        abcd21 = ET.SubElement(abcd16, "cmn:PostalCode")
        abcd21.text = str(postalcode)
        abcd22 = ET.SubElement(abcd16, "cmn:Country")
        abcd22.text = str(country)
        abcd23 = ET.SubElement(abcd13, "cmn:ShipFromLocationInfo")
        abcd24 = ET.SubElement(abcd23, "cmn:FacilityId" , attrib={'type':'GLN'})
        abcd24.text = str(factilty_type2value)
        abcd25 = ET.SubElement(abcd23, "cmn:FacilityId" , attrib={'type':'SGLN'})
        abcd25.text = str(factilty_type1value)
        abcd26 = ET.SubElement(abcd23,"cmn:LocationInfo")
        
        abcd27 = ET.SubElement(abcd26, "cmn:BusinessName")
        abcd27.text = str(detailobjb2.name)
        abcd28 = ET.SubElement(abcd26, "cmn:Street1")
        abcd28.text = str(street2)
        
        abcd29 = ET.SubElement(abcd26, "cmn:City")
        abcd29.text =str(city2)
        abcd30 = ET.SubElement(abcd26, "cmn:StateOrRegion")
        abcd30.text = str(State_or_region2)
        abcd31 = ET.SubElement(abcd26, "cmn:PostalCode")
        abcd31.text = str(postalcode2)
        abcd39 = ET.SubElement(abcd26, "cmn:District")
        abcd39.text = str(district)
        abcd32 = ET.SubElement(abcd26, "cmn:Country")
        abcd32.text = str(country2)  
        
        ######################### END LOOP
        abc33 = ET.SubElement(ab2, "cmn:ReceiverInfo")
       
        abc34 = ET.SubElement(abc33, "cmn:ToBusinessPartyLookupId" ,attrib={'type':'GLN'})
        abc34.text = str(to_business_part_lookupid)  
        abc35 = ET.SubElement(abc33, "cmn:ShipToLocationLookupId" ,attrib={'type':'COMPANYSITEID'})
        abc35.text = str(to_shiptolocationlookupid)  
        ab3 = ET.SubElement(a2, "som:AddPickedLot")
        abc36 = ET.SubElement(ab3, "cmn:ProductLotNumbers")
        abc37 = ET.SubElement(abc36, "cmn:InternalMaterialCode")
        abc37.text = str(internal_material_code)  
        abc38 = ET.SubElement(abc36, "cmn:LotNumber")
        abc38.text =str(lot_number)  
        abc7 = ET.SubElement(abcd5, "cmn:ExpirationDate")
        abc7.text = "2025-12-31"
        tree = ET.ElementTree(root)
        processordernumber=request.data["process_no_original"]
           
        # with open("xmlfiles/shipping.xml", "wb") as files:
        with open("xmlfiles/"+processordernumber+"_shipment.xml", "wb") as files:
            ET.indent(tree, '  ')
            tree.write(files,encoding='utf-8', xml_declaration=True)                        
        return Response(200)  

    


                            
# class Commissioningxml(APIView):
#     def get(self, request,id):
#         detailObj=Shipmentfiledata.objects.get(id=id)
        
#         # tree=ET.parse("xmlfiles/commissioning.xml")
        
#         # ET.register_namespace("","urn:tracelink:mapper:sl:serial_number_exchange")
#         # # frag_xml_tree.write("xmlfiles/commissioning.xml")
#         # root=tree.getroot()
#         root = ET.Element("SNXDispositionAssignedMessage")
#         root.set(r"xsi:schemaLocation",r"urn:tracelink:mapper:sl:serial_number_exchange C:\Users\lucy\Documents\TRACEL~1\PRODUC~1\SERIAL~1\SOMGRS~1\TL_XML_SerialNumberDispositionAssigned_2_0.xsd")
#         root.set(r"xmlns:xsi",r"http://www.w3.org/2001/XMLSchema-instance")
#         root.set(r"xmlns:cmn",r"urn:tracelink:mapper:sl:commontypes")
#         root.set(r"xmlns",r"urn:tracelink:mapper:sl:serial_number_exchange")
#         root.set(r"xmlns:snx",r"urn:tracelink:mapper:sl:serial_number_exchange")
#         ET.dump(root)
#         # ,attrib={'xsi:schemaLocation':'urn:tracelink:mapper:sl:serial_number_exchange C:\Users\lucy\Documents\TRACEL~1\PRODUC~1\SERIAL~1\SOMGRS~1\TL_XML_SerialNumberDispositionAssigned_2_0.xsd', 'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance" xmlns:cmn:"urn:tracelink:mapper:sl:commontypes','xmlns:cmn':'urn:tracelink:mapper:sl:commontypes','xmlns':'urn:tracelink:mapper:sl:serial_number_exchange" xmlns:snx="urn:tracelink:mapper:sl:serial_number_exchange','xmlns:snx':'urn:tracelink:mapper:sl:serial_number_exchange'}
#         a1 = ET.Element("snx:ControlFileHeader")
#         root.append(a1)
#         ab1 =ET.SubElement(a1, "cmn:FileSenderNumber")
#         ab1.text = str(detailObj.filetime)
#         ab2 = ET.SubElement(a1, "cmn:FileReceiverNumber")
#         ab2.text = "+05:30"
#         ab3 = ET.SubElement(a1, "cmn:FileControlNumber")
#         ab3.text = "20230223153249.145"
#         ab4 = ET.SubElement(a1, "cmn:FileDate")
#         ab4.text = "2023-02-23"
#         ab5 = ET.SubElement(a1, "cmn:FileTime")
#         ab5.text = "10:02:49Z"
#         a2 = ET.Element("snx:MessageBody")
#         root.append(a2)
#         ab2 = ET.SubElement(a2, "snx:CommissionEvent")
#         ########################## iNSIDE LOOP
#         for i in range(10):
#             abc2 = ET.SubElement(ab2, "snx:CommissionEventDetail")
#             abcd2 = ET.SubElement(abc2, "cmn:EventDateTime")
#             abcd2.text = "2023-02-10T11:15:05.358Z"
#             abcd3 = ET.SubElement(abc2, "cmn:EventTimeZoneOffset")
#             abcd3.text = "+05:30"
#             abcd4 = ET.SubElement(abc2, "cmn:SerialNumber")
#             abcd4.text = "01050991519180932121C6GWH87X"
#             abcd5 = ET.SubElement(abc2, "cmn:PackagingLevel")
#             abcd5.text = "EA"
#         ######################### END LOOP
#         abc3 = ET.SubElement(ab2, "snx:CommissionCommonAttributes")
#         abcd3 = ET.SubElement(abc3, "cmn:EventLocation")
#         abcd3.text = "506029274.000.0"
#         abcd4 = ET.SubElement(abc3, "cmn:ProductionLineId")
#         abcd4.text = "1"
#         abcd5 = ET.SubElement(abc3, "snx:ItemDetail")
#         abcde5 = ET.SubElement(abcd5, "cmn:InternalMaterialCode")
#         abcde5.text = "1305117"
#         abcde6 = ET.SubElement(abcd5, "cmn:LotNumber")
#         abcde6.text = "B30119"
#         abcde7 = ET.SubElement(abcd5, "cmn:ExpirationDate")
#         abcde7.text = "2025-12-31"
#         tree = ET.ElementTree(root)
#         with open("xmlfiles/commissioning.xml", "wb") as files:
#             ET.indent(tree, '  ')
#             tree.write(files,encoding='utf-8', xml_declaration=True)                        
#         return Response(200)    
      
      
class Destroyingxml(APIView):
    def post(self, request):
        # detailObj=Shipmentfiledata.objects.get(id=id)
        try:
            FileSenderNumber=request.data['filesendernumber']
        except:
            return Response(250)
        try:
            FileReceiverNumber=request.data['filereceivernumber']
        except:
            return Response(300)    
        try:
            FileControlNumber=request.data['filecontrolnumber']
        except:
            return Response(350)
            
        try:
            FileDate=request.data['filedate']
        except:
             return Response(400)
        try:
            EventDateTime=request.data['EventTimeZoneOffset']
        except:
             return Response(450)
        try:
             Filetime=request.data['filetime']
        except:
             return Response(500)
        # SerialNumbers=request.data['filesendernumber']
        PackagingSerialNumberStatus=request.data['packagingstatus']
        ItemAttribute=request.data['itemAttribute']
        EventLocation=request.data['eventLocation']
        ReasonDescription=request.data['reasonDescription']
        
        ponumber=request.data['process_no_original']
        
        
        try:
            detailsobj2 = ShipPO.objects.get(process_no_original=ponumber)
            prodObj=PrinterdataTable.objects.get(processordernumber=detailsobj2.process_no_original)
            cin=json.loads(str(prodObj.Rejectednumbers))
        except:
            return Response(100)
        
        stringjson=str(cin)
        lengthdestroy=len(cin)
        gtinno=prodObj.gtin
        new1arry=[]
        for i in range(lengthdestroy):
                                
            new1arry.append(str(gtinno)+str(cin[i]))
            
            print(new1arry)
        
        # print(lengthdestroy)
         
                             
       
        
        # tree=ET.parse("xmlfiles/commissioning.xml")
        
        # ET.register_namespace("","urn:tracelink:mapper:sl:serial_number_exchange")
        # # frag_xml_tree.write("xmlfiles/commissioning.xml")
        # root=tree.getroot()
        
        root = ET.Element("snx:SNXDispositionUpdatedMessage")
        root.set(r"xmlns:xsi",r"http://www.w3.org/2001/XMLSchema-instance")
        root.set(r"xmlns:cmn",r"urn:tracelink:mapper:sl:commontypes")
        root.set(r"xmlns:snx",r"urn:tracelink:mapper:sl:serial_number_exchange")
        root.set(r"xmlns",r"urn:tracelink:mapper:sl:serial_number_exchange")
     
        ET.dump(root)
        # ,attrib={'xsi:schemaLocation':'urn:tracelink:mapper:sl:serial_number_exchange C:\Users\lucy\Documents\TRACEL~1\PRODUC~1\SERIAL~1\SOMGRS~1\TL_XML_SerialNumberDispositionAssigned_2_0.xsd', 'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance" xmlns:cmn:"urn:tracelink:mapper:sl:commontypes','xmlns:cmn':'urn:tracelink:mapper:sl:commontypes','xmlns':'urn:tracelink:mapper:sl:serial_number_exchange" xmlns:snx="urn:tracelink:mapper:sl:serial_number_exchange','xmlns:snx':'urn:tracelink:mapper:sl:serial_number_exchange'}
        a1 = ET.Element("snx:ControlFileHeader")
        root.append(a1)
        ab1 =ET.SubElement(a1, "cmn:FileSenderNumber")
        ab1.text = str(FileSenderNumber)
        ab2 = ET.SubElement(a1, "cmn:FileReceiverNumber")
        ab2.text =str(FileReceiverNumber)
        ab3 = ET.SubElement(a1, "cmn:FileControlNumber")
        ab3.text = str(FileControlNumber)
        ab4 = ET.SubElement(a1, "cmn:FileDate")
        ab4.text = str(FileDate)
        ab5 = ET.SubElement(a1, "cmn:FileTime")
        ab5.text = str(Filetime)
        a2 = ET.Element("snx:MessageBody")
        root.append(a2)
        abc2 = ET.SubElement(a2, "cmn:EventDateTime")
        abc2.text = str(EventDateTime)
        abc3 = ET.SubElement(a2, "cmn:EventTimeZoneOffset")
        abc3.text = str(FileSenderNumber)
        ab2 = ET.SubElement(a2, "snx:SerialNumbers")
        ########################## iNSIDE LOOP
        # for i in range(10):
        i=0
        while i < lengthdestroy:
      
            abc4 = ET.SubElement(ab2, "cmn:Serial")
            abc4.text = str(new1arry[i])
            i=i+1    
        
        ######################### END LOOP
        abc5 = ET.SubElement(a2,"cmn:PackagingSerialNumberStatus")
        abc5.text = str( PackagingSerialNumberStatus)
      
        abc6 = ET.SubElement(a2, "cmn:ItemAttribute")
        abc6.text = str(ItemAttribute)
        abc7 = ET.SubElement(a2, "cmn:EventLocation")
        abc7.text = str(EventLocation)
        abc8 = ET.SubElement(a2, "cmn:ReasonDescription")
        abc8.text = str( ReasonDescription)
       
        tree = ET.ElementTree(root)
        processordernumber=request.data["process_no_original"] 
        with open("xmlfiles/"+ processordernumber+"_po_destroy.xml", "wb") as files:
            ET.indent(tree, '  ')
            tree.write(files,encoding='utf-8', xml_declaration=True)
            print("genetated")                        
        return Response(200)    
            
class Commissioningxml(APIView):
    # def get(self, request,id):
    #     detailObj=Commisioningxml.objects.get(id=id)
    #     serializeobj=CommissioningxmldataSerializer(detailObj,many=True)
    #     return Response(serializeobj.data)
        
        # tree=ET.parse("xmlfiles/commissioning.xml")
        
        # ET.register_namespace("","urn:tracelink:mapper:sl:serial_number_exchange")
        # # frag_xml_tree.write("xmlfiles/commissioning.xml")
        # root=tree.getroot()
    # def post(self,request):
    #     serializeobj=CommissioningxmldataSerializer(data=request.data)
    #     serialno=request.data['serialnumber']
    #     if serializeobj.is_valid():
    #         # try:
    #         device=serializeobj.save()
            
    #     detailObj=Commisioningxml.objects.get(pk=device.id)
    #         # obj = Commissioningxml.objects.get(pk=device.id)
    #     detailObj=Commisioningxml.objects.get(pk=device.id)   
    #     obj=Commissioningxml.objects.filter(pk=device.id).update(serialnumber=serialno)
    #         #     return Response(200)
    #         # except:
    #         #      return Response(401)
                
        
        
       
      
    #     detailObj1=Commisioningxml.objects.get(pk=device.id)
    #     # snarray=[]
    #     # # print(serialno)
    #     # # parseserialno=json.loads(serialno)
    #     # snarray.append(serialno)
    #     # jsonString = json.dumps(snarray)
       
    #     # print(seriallist)
    #     lengthserialno=len(serialno)
    #     print(lengthserialno)
    def post(self,request):         
            
        # serializeobj=CommissioningxmldataSerializer(data=request.data)
        
        # if serializeobj.is_valid():
        #     device=serializeobj.save()
            
        processordernumber=request.data["process_no_original"] 
       
        # EventTimeZoneOffset=request.data["EventTimeZoneOffset"]
        # eventdatetime= request.data["eventdatetime"]
        # filecontrolnumber=request.data["filecontrolnumber"]
        try:
            filereceivernumber=request.data["filereceivernumber"]
        except:
            return Response(100)  
        try:
            filesenderno=request.data["filesendernumber"]
        except:
            return Response(300) 
        try: 
            detailobjfilesenderno=Locations.objects.get(id=filesenderno)
        
            filedate=request.data["filedate"]
        except: 
            return Response(400) 
        
        try: 
            filetime=request.data["filetime"]
        except:
            return Response(500)
        try:
            lotnumber=request.data["lotnumber"]
        except:
            return Response(600)
       
        try:
            serialno=request.data['serialnumber']
        except:
            return Response(700)
        try:
            EventTimeZoneOffset=request.data["EventTimeZoneOffset"]
        except:
             return Response(800)
        
       
       
        try:
              filecontrolnumber=request.data["filecontrolnumber"]
        except:
            return Response(900)
            # eventdatetime=request.data["eventdatetime"]
        # if(filereceivernumber==""):
        #     return Response(200)   
        try:
            detailsObj1=ProductionOrder.objects.get(process_order_number= processordernumber)

            internal_material_code=detailsObj1.internal_material_number
        except:
            return Response(950)     
      
        try:    
            detailsObjexp=ProductionOrder.objects.get(process_order_number= processordernumber)

            expirationdate=detailsObjexp.expiration_date
           
        except:
            return Response(1000) 

        try: 
            
            detailsObjproductionLineId=ProductionOrder.objects.get(process_order_number= processordernumber)

            productionLineId=detailsObjproductionLineId.line
                
            
        except:
            return Response(1050)  
            
        snarray=[]
       
        print(serialno)
            # parseserialno=json.dumps(serialno)
        loadjson=json.loads(str(serialno)) 
            # print(loadjson)
        lengthserialno=len(str(loadjson))
                             
        eventLocation=request.data["eventLocation"]   
        packagingLevel=request.data["packagingLevel"]    
              
            
                          
                # print(temp)                  
            
            # obj = Commisioningxml.objects.get(pk=device.id)
                
            # detailObj=Commisioningxml.objects.filter(pk=device.id).update(serialnumber=serialno)
               
                
                
            # detailObj1=Commisioningxml.objects.get(pk=device.id)
            
                            
                                
        root = ET.Element("SNXDispositionAssignedMessage")
        root.set(r"xsi:schemaLocation",r"urn:tracelink:mapper:sl:serial_number_exchange C:\Users\lucy\Documents\TRACEL~1\PRODUC~1\SERIAL~1\SOMGRS~1\TL_XML_SerialNumberDispositionAssigned_2_0.xsd")
        root.set(r"xmlns:xsi",r"http://www.w3.org/2001/XMLSchema-instance")
        root.set(r"xmlns:cmn",r"urn:tracelink:mapper:sl:commontypes")
        root.set(r"xmlns",r"urn:tracelink:mapper:sl:serial_number_exchange")
        root.set(r"xmlns:snx",r"urn:tracelink:mapper:sl:serial_number_exchange")
        ET.dump(root)
                # ,attrib={'xsi:schemaLocation':'urn:tracelink:mapper:sl:serial_number_exchange C:\Users\lucy\Documents\TRACEL~1\PRODUC~1\SERIAL~1\SOMGRS~1\TL_XML_SerialNumberDispositionAssigned_2_0.xsd', 'xmlns:xsi':'http://www.w3.org/2001/XMLSchema-instance" xmlns:cmn:"urn:tracelink:mapper:sl:commontypes','xmlns:cmn':'urn:tracelink:mapper:sl:commontypes','xmlns':'urn:tracelink:mapper:sl:serial_number_exchange" xmlns:snx="urn:tracelink:mapper:sl:serial_number_exchange','xmlns:snx':'urn:tracelink:mapper:sl:serial_number_exchange'}
        a1 = ET.Element("snx:ControlFileHeader")
        root.append(a1)
        ab1 =ET.SubElement(a1, "cmn:FileSenderNumber")
        ab1.text = str(detailobjfilesenderno.name)
        ab2 = ET.SubElement(a1, "cmn:FileReceiverNumber")
        ab2.text = str(filereceivernumber)
        ab3 = ET.SubElement(a1, "cmn:FileControlNumber")
        ab3.text = str(filecontrolnumber)
        ab4 = ET.SubElement(a1, "cmn:FileDate")
        ab4.text = str(filedate)
        ab5 = ET.SubElement(a1, "cmn:FileTime")
        ab5.text = str(filetime)
        a2 = ET.Element("snx:MessageBody")
        root.append(a2)
        ab2 = ET.SubElement(a2, "snx:CommissionEvent")
                ########################## iNSIDE LOOP
        i=0
        while i < len(loadjson):
          
            abc2 = ET.SubElement(ab2, "snx:CommissionEventDetail")
            abcd2 = ET.SubElement(abc2, "cmn:EventDateTime")
            abcd2.text = str("20-3-23")
            abcd3 = ET.SubElement(abc2, "cmn:EventTimeZoneOffset")
            abcd3.text = str(EventTimeZoneOffset)
            abcd4 = ET.SubElement(abc2, "cmn:SerialNumber")
            # print(loadjson[i])             
                # i = i + 1 
            abcd4.text = str(loadjson[i])
             
                
            abcd5 = ET.SubElement(abc2, "cmn:PackagingLevel")
            abcd5.text =str(packagingLevel)
            i = i + 1 
                ######################### END LOOP
        abc3 = ET.SubElement(ab2, "snx:CommissionCommonAttributes")
        abcd3 = ET.SubElement(abc3, "cmn:EventLocation")
        abcd3.text = str(eventLocation)
        abcd4 = ET.SubElement(abc3, "cmn:ProductionLineId")
        abcd4.text = str(productionLineId)
        abcd5 = ET.SubElement(abc3, "snx:ItemDetail")
        abcde5 = ET.SubElement(abcd5, "cmn:InternalMaterialCode")
        abcde5.text = str(internal_material_code)
        abcde6 = ET.SubElement(abcd5, "cmn:LotNumber")
        abcde6.text = str(lotnumber)
        abcde7 = ET.SubElement(abcd5, "cmn:ExpirationDate")
        abcde7.text = str(expirationdate)
                
        tree = ET.ElementTree(root)
        processordernumber=request.data["process_no_original"] 
        with open("xmlfiles/"+ processordernumber+"_po_commissioning.xml", "wb") as files:
            ET.indent(tree, '  ')
            tree.write(files,encoding='utf-8', xml_declaration=True)
                
                # path = '/SerialNumbers'
                # ftp = ftplib.FTP("aplusintellitech.com")
                # ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

                # ftp.cwd(path)
                # # detailObj=Commisioningxml.objects.all()
                # # serializeobj=CommissioningxmldataSerializer(detailObj,many=True)
                # # if serializeobj.is_valid():
                # #     device=serializeobj.save()
                
                

               
                # file = open('D:/serial numbers CSV file.csv','rb')
                # # file to send
                # processordernumber=request.data["process_no_original"]
                # file_path = Path("xmlfiles/"+ processordernumber+"_po_commissioning.xml")
                
                # ftp.storbinary(f'STOR {file_path.name}', file)     # send the file
                # file.close()                                    # close file and FTP
                # ftp.quit()
                            
        return Response(200)        
    
class Uploadcommissioningxml(APIView):
                                        
    def post(self, request):
        path = '/SerialNumbers'
        ftp = ftplib.FTP("aplusintellitech.com")
        ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        ftp.cwd(path)
                
                

        processordernumber=request.data["process_order_number"]       
        # file = open('D:/serial numbers CSV file.csv','rb')
        file = open("xmlfiles/"+ processordernumber+"_po_commissioning.xml",'rb')
                # file to send
       
        file_path = Path("xmlfiles/"+ processordernumber+"_po_commissioning.xml")
                
        ftp.storbinary(f'STOR {file_path.name}', file)     # send the file
        file.close()                                    # close file and FTP
        ftp.quit()
        
        
    



        return Response(200)
    
class Uploadshipmentxml(APIView):
                                        
    
        
        
    def post(self, request):
        path = '/SerialNumbers'
        ftp = ftplib.FTP("aplusintellitech.com")
        ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        ftp.cwd(path)
                
                
        processordernumber=request.data["process_order_number"]
        file = open("xmlfiles/"+ processordernumber+"_shipment.xml",'rb')       
        # file = open('D:/serial numbers CSV file.csv','rb')
                # file to send
        processordernumber=request.data["process_order_number"]
        file_path = Path("xmlfiles/"+ processordernumber+"_shipment.xml")
                
        ftp.storbinary(f'STOR {file_path.name}', file)     # send the file
        file.close()                                    # close file and FTP
        ftp.quit()



        return Response(200)
    
    
class UploadDestroyxml(APIView):
                                        
    
        
        
    def post(self, request):
        path = '/SerialNumbers'
        ftp = ftplib.FTP("aplusintellitech.com")
        ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        ftp.cwd(path)
                
                
        processordernumber=request.data["process_order_number"]
        file = open("xmlfiles/"+ processordernumber+"_po_destroy.xml",'rb')       
        # file = open('D:/serial numbers CSV file.csv','rb')
                # file to send
        processordernumber=request.data["process_order_number"]
        file_path = Path("xmlfiles/"+ processordernumber+"_po_destroy.xml")
                
        ftp.storbinary(f'STOR {file_path.name}', file)     # send the file
        file.close()                                    # close file and FTP
        ftp.quit()



        return Response(200)     
    
class Downloadshipmentxml(APIView):
                                        
    
        
        
    def post(self, request):
        path = '/SerialNumbers'
        ftp = ftplib.FTP("aplusintellitech.com")
        ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        ftp.cwd(path)
                
                

        path = '/SerialNumbers'
        processordernumber=request.data["process_order_number"]
        # downloadstatus=request.data["downloadstatus_shipment"]
        # if  downloadstatus=='true':

        filename =  processordernumber+"_shipment.xml"
            # filename = "60_po_commissioning.xml"
            # filename = "10_shipment.xml"




        ftp = ftplib.FTP("aplusintellitech.com")

        ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        ftp.cwd(path)

        ftp.retrbinary("RETR " + filename, open("D:\XMLFILEDATA/"+ processordernumber+"_shipment.xml", 'wb').write)

        ftp.quit()
            

        return Response(200)   
    
class Downloadcommissioningxml(APIView):
                                        
    
        
        
    def post(self, request):
        path = '/SerialNumbers'
        ftp = ftplib.FTP("aplusintellitech.com")
        ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        ftp.cwd(path)
                
                

        path = '/SerialNumbers'
        processordernumber=request.data["process_order_number"]

        filename =  processordernumber+"_po_commissioning.xml"
        # filename = "60_po_commissioning.xml"
        # filename = "10_shipment.xml"




        ftp = ftplib.FTP("aplusintellitech.com")

        ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        ftp.cwd(path)

        ftp.retrbinary("RETR " + filename, open("D:\XMLFILEDATA/"+ processordernumber+"_po_commissioning.xml", 'wb').write)

        ftp.quit()
            

        return Response(200)     
    
class Downloaddestroyxml(APIView):
                                        
    
        
        
    def post(self, request):
        path = '/SerialNumbers'
        ftp = ftplib.FTP("aplusintellitech.com")
        ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        ftp.cwd(path)
                
                

        path = '/SerialNumbers'
        processordernumber=request.data["process_order_number"]
        # downloadstatus=request.data["downloadstatus_destroy"]
        # print(downloadstatus)
        # if(downloadstatus==True):

        filename =  processordernumber+"_po_destroy.xml"
            # filename = "60_po_commissioning.xml"
            # filename = "10_shipment.xml"




        ftp = ftplib.FTP("aplusintellitech.com")

        ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        ftp.cwd(path)

        ftp.retrbinary("RETR " + filename, open("D:\XMLFILEDATA/"+ processordernumber+"_po_destroy.xml", 'wb').write)

        ftp.quit()
            

        return Response(200)                
    
    
# class Downloadallxmlfiles(APIView):
#     def post(self, request):
#         path = '/SerialNumbers'
#         ftp = ftplib.FTP("aplusintellitech.com")
#         ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

#         ftp.cwd(path)
                
                

       
#         processordernumber=request.data["process_order_number"]
#         downloadstatus=request.data["downloadstatus_allxml"]
#         if(downloadstatus==True):

#             filename =  processordernumber+"_shipment.xml"
#             # filename = "60_po_commissioning.xml"
#             # filename = "10_shipment.xml"




#             ftp = ftplib.FTP("aplusintellitech.com")

#             ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

#             ftp.cwd(path)

#             ftp.retrbinary("RETR " + filename, open("D:\XMLFILEDATA/"+ processordernumber+"_shipment.xml", 'wb').write)
#             # file_name = "D:\XMLFILEDATA/"+ processordernumber+"_shipment.xml"
#             # with ZipFile(file_name, 'w') as zip:
#             # # with ZipFile("D:/"+ processordernumber+"_po_destroy.zip",'w') as zip:
#             # # # writing each file one by one
#             #     for file in filename:
#             #         zip.write(file) 

#             ftp.quit()
            
            
#     # # def post(self, request):
#             path = '/SerialNumbers'
#             ftp = ftplib.FTP("aplusintellitech.com")
#             ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

#             ftp.cwd(path)
                    
                    

           
#             processordernumber=request.data["process_order_number"]
#             # downloadstatus=request.data["downloadstatus_allxml"]
#             # if  downloadstatus=='true':

#             filename =  processordernumber+"_po_commissioning.xml"
#                 # filename = "60_po_commissioning.xml"
#                 # filename = "10_shipment.xml"




#             ftp = ftplib.FTP("aplusintellitech.com")

#             ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

#             ftp.cwd(path)

#             ftp.retrbinary("RETR " + filename, open("D:\XMLFILEDATA/"+ processordernumber+"_po_commissioning.xml", 'wb').write)
#             # file_name = "D:\XMLFILEDATA/"+ processordernumber+"_po_commissioning.xml"
#             # with ZipFile(file_name, 'w') as zip:
#             # # with ZipFile("D:/"+ processordernumber+"_po_destroy.zip",'w') as zip:
#             # # # writing each file one by one
#             #     for file in filename:
#             #         zip.write(file) 

#             ftp.quit()
            
            
#         # def post(self, request):
#             path = '/SerialNumbers'
#             ftp = ftplib.FTP("aplusintellitech.com")
#             ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

#             ftp.cwd(path)
                    
                    

#             path = '/SerialNumbers'
#             processordernumber=request.data["process_order_number"]
#             # downloadstatus=request.data["downloadstatus_allxml"]
#             # if  downloadstatus=='true':

#             filename =  processordernumber+"_po_destroy.xml"
#                 # filename = "60_po_commissioning.xml"
#                 # filename = "10_shipment.xml"




#             ftp = ftplib.FTP("aplusintellitech.com")

#             ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

#             ftp.cwd(path)
            

#             ftp.retrbinary("RETR " + filename, open("D:\XMLFILEDATA/"+ processordernumber+"_po_destroy.xml", 'wb').write)
#             # file_name = "D:\XMLFILEDATA/"+ processordernumber+"_po_destroy.xml"
#             # with ZipFile(file_name, 'w') as zip:
#             # # with ZipFile("D:/"+ processordernumber+"_po_destroy.zip",'w') as zip:
#             # # # writing each file one by one
#             #     for file in filename:
#             #         zip.write(file) 

#             ftp.quit()
                
                                    
#         return Response(200)     
    
    
class Downloadallxmlfiles(APIView):
    def post(self, request):
        path = '/SerialNumbers'
        ftp = ftplib.FTP("aplusintellitech.com")
        ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

        ftp.cwd(path)
                
                

       
        processordernumber=request.data["process_order_number"]
        downloadstatus=request.data["downloadstatus_allxml"]
        if(downloadstatus==True):

            filename =  processordernumber+"_shipment.xml"
            # filename = "60_po_commissioning.xml"
            # filename = "10_shipment.xml"
           
  



            ftp = ftplib.FTP("aplusintellitech.com")

            ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

            ftp.cwd(path)

            ftp.retrbinary("RETR " + filename, open("D:\XMLDOWNLOADEDFILES/"+ processordernumber+"_shipment.xml", 'wb').write)
            
            ftp.quit()
            
            
            
    # # def post(self, request):
            path = '/SerialNumbers'
            ftp = ftplib.FTP("aplusintellitech.com")
            ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

            ftp.cwd(path)
                    
                    

           
            processordernumber=request.data["process_order_number"]
            # downloadstatus=request.data["downloadstatus_allxml"]
            # if  downloadstatus=='true':

            filename =  processordernumber+"_po_commissioning.xml"
                # filename = "60_po_commissioning.xml"
                # filename = "10_shipment.xml"
        
            ftp = ftplib.FTP("aplusintellitech.com")

            ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

            ftp.cwd(path)

            ftp.retrbinary("RETR " + filename, open("D:\XMLDOWNLOADEDFILES/"+ processordernumber+"_po_commissioning.xml", 'wb').write)
            
            ftp.quit()
            
            
        # def post(self, request):
            path = '/SerialNumbers'
            ftp = ftplib.FTP("aplusintellitech.com")
            ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

            ftp.cwd(path)
                    
                    

            path = '/SerialNumbers'
            processordernumber=request.data["process_order_number"]
            # downloadstatus=request.data["downloadstatus_allxml"]
            # if  downloadstatus=='true':

            filename =  processordernumber+"_po_destroy.xml"
                # filename = "60_po_commissioning.xml"
                # filename = "10_shipment.xml"
            file_name = "D:\XMLFILEDATA/file.zip"




            ftp = ftplib.FTP("aplusintellitech.com")

            ftp.login("TrackNTrace@aplusintellitech.com","TrackNTrace")

            ftp.cwd(path)
            

            ftp.retrbinary("RETR " + filename, open("D:\XMLDOWNLOADEDFILES/"+ processordernumber+"_po_destroy.xml", 'wb').write)
          
              
           
                  
            

            ftp.quit()
            
            directory = "D:\XMLDOWNLOADEDFILES/"
            file_paths = []
            for root, directories, files in os.walk(directory):
                for filename in files:
            # join the two strings in order to form the full filepath.
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)
                    
                with ZipFile('D:\XMLFILEDATA/xml_files.zip','w') as zip:
       
                    for file in file_paths:
                        zip.write(file)
                
                                    
        return Response(200)
#   ...................................................................///
class Balancedserialnumberview(APIView):
    def post(self,request):
        id=request.data["id"]
        gtin=request.data["gtin"]
        lot=request.data["batch_number"]
        detailsObj = ProductionOrder.objects.get(id=id) 
        prodObj=PrinterdataTable.objects.get(lot=detailsObj.batch_number)
        balance_slno_json=prodObj.balanced_serialnumbers
        balance_slno_list= json.loads(balance_slno_json)
        # print(balance_slno_json)
        # balance_slno_list=json.loads(balance_slno_json)
       
        # df=pd.read_csv("csvfiles/"+gtin+".csv")
        indexlist=[]
        # print(gtin)
        with open("csvfiles/"+gtin+".csv", newline='') as file:

            readobj=csv.reader(file)
            last_row = None
            for row in readobj:
                if row:  # This skips blank lines
                    last_row = row
            i=int(last_row[0])+1       

        
        


        with open("csvfiles/"+gtin+".csv", 'a', newline='') as file:
                    for t in balance_slno_list:                                
                        writer = csv.writer(file)
                        valuelist = [i,gtin,t,"notallow"],
                        writer.writerows(valuelist)
                        i=i+1
        detailsObj5 = ProductionOrder.objects.get(batch_number=lot)
        Obj=ProductionOrder.objects.filter(batch_number=detailsObj5.batch_number).update(btncontrollstatus="Numbers Returened") 
        return Response(200)

        # ....................................................
        
        # with open("Allocatedcsv/"+gtin+".csv", newline='') as t:
        #     readobj=csv.reader(t)
            
        #     for row in readobj:
        #           if row[3] =='unallocated' :
        #                 # print( row[3])
                     
        #                 with open("csvfiles/"+gtin+'.csv', 'a', encoding='UTF8',newline='') as f:
                            
        #                     i=0           # print(row)
                                      
        #                     writer = csv.writer(f)
                                    
        #                     valuelist = [gtin,t, "unallocated",],
        #                     writer.writerows(row)
        #                     i=i+1
        
        # with open("Allocatedcsv/"+gtin+".csv","r") as demo2:
    # # creating reader object
    #         csv_reader=csv.reader(demo2)
    # # reading the file
    #         data=[]
    #         for row in csv_reader:
    #             if row[3]=="unallocated":
    #                 data.append(row)       
    #     with open("csvfiles/"+gtin+'.csv',"a",newline="") as demo1:
            
    #         # creating writer object
    #         csv_writer=csv.writer(demo1)
    #         # appending data
    #         csv_writer.writerows(data[1:])       
       
# .............................................................................

# BACKUP DATAS CODE

class TrashCompany(APIView):
    def delete(self, request, pk):
        try:
            detailsObj =Company.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = Company.objects.all().filter(id=pk)
        detailObj=Company.objects.filter(id=pk).update(companyflag=True)
      
       
        historySave = History(modelname='company',
                              savedid=pk,
                              operationdone='deletetotrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Deleted the company " +request.data['company_name'] +" to trash")
        historySave.save()
        return Response(200)

class RestoreTrashCompany(APIView):
    def delete(self, request, pk):
        company_name=request.data['company_name']
        try:
            detailsObj = Company.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = Company.objects.all().filter(id=pk)
        detailObj=Company.objects.filter(id=pk).update(companyflag=False)
       
       
        historySave = History(modelname='company',
                              savedid=pk,
                              operationdone='restorefromtrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Restored the company " + company_name +" from trash")
        historySave.save()
        return Response(200)

    
class TrashCustomer(APIView):
    def delete(self, request, pk):
        try:
            detailsObj =Customers.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = Customers.objects.all().filter(id=pk)
        detailObj=Customers.objects.filter(id=pk).update(customerflag=True)
      
       
        historySave = History(modelname='customer',
                              savedid=pk,
                              operationdone='deletetotrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Deleted the customer " +request.data['name'] +" to trash")
        historySave.save()
        return Response(200)

class RestoreTrashCustomer(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Customers.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = Customers.objects.all().filter(id=pk)
        detailObj=Customers.objects.filter(id=pk).update(customerflag=False)
       
       
        historySave = History(modelname='customer',
                              savedid=pk,
                              operationdone='restorefromtrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Restored the customer " +request.data['name'] + " from trash")
        historySave.save()
        return Response(200)    
    

  
class TrashCustomerLocation(APIView):
    def delete(self, request, pk):
        try:
            detailsObj =Locations.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = Locations.objects.all().filter(id=pk)
        detailObj=Locations.objects.filter(id=pk).update(locationflag=True)
      
       
        historySave = History(modelname='customerlocation',
                              savedid=pk,
                              operationdone='deletetotrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Deleted the customerlocation " +request.data['name'] +" to trash")
        historySave.save()
        return Response(200)

class RestoreTrashCustomerLocation(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Locations.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = Locations.objects.all().filter(id=pk)
        detailObj=Locations.objects.filter(id=pk).update(locationflag=False)
       
       
        historySave = History(modelname='customerlocation',
                              savedid=pk,
                              operationdone='restorefromtrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Restored the customerlocation " +request.data['name'] + " from trash")
        historySave.save()
        return Response(200)  
                 
      
      
class TrashProduct(APIView):
    def delete(self, request, pk):
        try:
            detailsObj =Product.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = Product.objects.all().filter(id=pk)
        detailObj=Product.objects.filter(id=pk).update(productflag=True)
      
       
        historySave = History(modelname='product',
                              savedid=pk,
                              operationdone='deletetotrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Deleted the product " +request.data['name'] +" to trash")
        historySave.save()
        return Response(200)

class RestoreTrashProduct(APIView):
    def delete(self, request, pk):
        
        try:
            detailsObj = Product.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = Product.objects.all().filter(id=pk)
        detailObj=Product.objects.filter(id=pk).update(productflag=False)
       
       
        historySave = History(modelname='product',
                              savedid=pk,
                              operationdone='restorefromtrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Restored the product " + request.data["name"] +" from trash")
        historySave.save()
        return Response(200)                                                 
    
    
    
class TrashShippo(APIView):
    def delete(self, request, pk):
        try:
            detailsObj =ShipPO.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = ShipPO.objects.all().filter(id=pk)
        detailObj=ShipPO.objects.filter(id=pk).update(shippoflag=True)
      
       
        historySave = History(modelname='shippo',
                              savedid=pk,
                              operationdone='deletetotrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Deleted the shippingorder " +request.data['shipping_order_name'] +" to trash")
        historySave.save()
        return Response(200)

class RestoreTrashShippo(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ShipPO.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = ShipPO.objects.all().filter(id=pk)
        detailObj=ShipPO.objects.filter(id=pk).update(shippoflag=False)
       
       
        historySave = History(modelname='shippo',
                              savedid=pk,
                              operationdone='restorefromtrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Restored the shippingorder " +request.data['shipping_order_name'] + " from trash")
        historySave.save()
        return Response(200)   
    
class TrashProductionOrder(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ProductionOrder.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = ProductionOrder.objects.all().filter(id=pk)
        detailObj=ProductionOrder.objects.filter(id=pk).update(prodcutionorderflag=True)
        # detailsObj.delete()
       
        historySave = History(modelname='productionorder',
                              savedid=pk,
                              operationdone='deletetotrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Deleted the productionorder " + request.data['process_order_number'] + " to trash")
        historySave.save()
        return Response(200)

class RestoreTrashProductionOrder(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ProductionOrder.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = ProductionOrder.objects.all().filter(id=pk)
        detailObj=ProductionOrder.objects.filter(id=pk).update(prodcutionorderflag=False)
        # detailsObj.delete()
       
        historySave = History(modelname='productionorder',
                              savedid=pk,
                              operationdone='restorefromtrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Restored the productionorder " + request.data['process_order_number'] + " from trash")
        historySave.save()
        return Response(200)
    
# ....................................................................................
class ProdOrderReport(APIView):
    def get(self, request):
        detailsObj = ProdReport.objects.all()
        serializeObj = ProdReportSerializer(detailsObj, many=True)
        return Response(serializeObj.data)
    def post(self, request):
        serializeObj = ProdReportSerializer(data=request.data)
       
        if serializeObj.is_valid():
            serializeObj.save()
          
           
           
            
            
            return Response(200)
        return Response(serializeObj.errors)

class ProdOrderReportIndividual(APIView):
    def get(self, request, id):
        detailsObj = ProdReport.objects.all().filter(batch_number=id)
        serializeObj = ProdReportSerializer(detailsObj, many=True)
        return Response(serializeObj.data)
    #     try:
    #         detailsObj = ProductionReport.objects.get(batch_number=id)
    #     except:
    #         return Response("Not found in database")

    #     serializeObj = ProductionReportSerializer(detailsObj, data=request.data)
    #     if (serializeObj.is_valid()):
    #         return Response(serializeObj.data)

    #     return Response(serializeObj.errors)
class ProdOrderReportdate(APIView):  
    def get(self, request):
        detailsObj = ProdReport.objects.all()
        serializeObj = ProdReportSerializer(detailsObj, many=True)
        # fromDate = request.data["datefrom"]
        # toDate = request.data["dateto"]
        # response  = ProductionReport.objects.filter( production_date=fromDate, production_date__lte=toDate)
        return Response(200)
    
    def post(self, request):
        serializeObj = ProdReportSerializer(data=request.data)
        v=[]
        startdate = request.data["datefrom"]
        
        toDate = request.data["dateto"]
        # fromDate=str(request.POST.get('datefrom'))
        # toDate=str(request.POST.get("dateto"))
        # response  =ProductionReport.objects.all().filter(production_date=id)
        
        response  =ProdReport.objects.all().filter(production_date__range=(startdate, toDate))
        serializeObj = ProdReportSerializer(response , many=True)
        return Response(serializeObj.data)
# /////////////////////////////////////////////////////////////////////////////
class Allocatednumbersview(APIView) :
        def get(self,request):
            detailObj=Allocatednumbers.objects.all().order_by('-id')
            serializeobj=AllocatednumberSerializer(detailObj,many=True)
            return Response(serializeobj.data)
        
        
        
       
        
        
        def post(self,request):
            serializeobj=AllocatednumberSerializer(data=request.data)
            gtin=request.data['gtin_number']
            lot=request.data['batch_number']
            minq=request.data['quantity']
            loginname=request.data['loggedInUsername']
            loginuserrole=request.data['loggedInUserrole']
            print(gtin)
            print(lot)
            print(minq)
            try:
                obj = Gtins.objects.get(gtin=gtin)
                print(obj.available_quantity)
                Av_quty=obj.available_quantity
                maximum_number_of_quanty_allocated=100000
            except:
                return Response(500)    
            try:
                with open("csvfiles/"+gtin+".csv")  as f:
                                results = pd.read_csv("csvfiles/"+gtin+".csv")
                                count=len(results)
                                print(count)
                                if(count==0):
                                    return Response(600)
                                elif(int(minq )>maximum_number_of_quanty_allocated):
                                    return Response(700)  
                                elif(int(minq)>int(Av_quty)):
                                    return Response(800)                 
                if serializeobj.is_valid():
                    serializeobj.save()
                   
                    try:
                       
        
                        with open("csvfiles/"+gtin+".csv")  as f:
                                results = pd.read_csv("csvfiles/"+gtin+".csv")
                                count=len(results)
                                print(count)
                               
                                obj = Gtins.objects.get(gtin=gtin)
                                detailObj=Gtins.objects.all().filter(gtin=obj.gtin).update(available_quantity=count) 
                                print("availabe quantiyt upadateed to gtin model")   
                        # with open("csvfiles/"+gtin+".csv", newline='') as f:
                        #             readobj=csv.reader(f)
                        #             for row in readobj:
                        #                 t=row[2]
                                        # print(t)                    
                                
                                
                        row_list = ["SN", "Gtin", "Serialno","Status","SendingStatus","lot"],
                                
                                    
                                    # i=i+1
                        
                        with open("Allocatedcsv/"+lot+".csv", 'a', newline='') as file:
                                                
                                        writer = csv.writer(file)
                                        writer.writerows(row_list)
                                        i=-1
                                        k=0
                        with open("csvfiles/"+gtin+".csv", newline='') as f:
                                        readobj=csv.reader(f)
                                        for row in readobj:
                                            t=row[2]        
                                    
                                        
                                
                                
                                    
                                            i=i+1
                                            # k=k+1
                                            if(k>int(minq)):
                                                break
                                                            
                        
                                            with open("Allocatedcsv/"+lot+".csv", 'a', newline='') as file:
                                                
                                                writer = csv.writer(file)
                                                if(k!=0):
                                                    valuelist = [i,gtin,t, "allocated",minq,lot],
                                                    writer.writerows(valuelist)
                                                k=k+1
                                                slnolist=[]
                                                rowIndex=[]
                                                counter=1
                                                loopcounter=-1
                        with open("csvfiles/"+gtin+".csv", newline='') as f:

                                    readobj=csv.reader(f)

                                    for row in readobj:

                                        if(row[3]=="notallow"):

                                            slnolist.append(row[2])

                                            rowIndex.append(loopcounter)

                                            counter=counter+1

                                        if(counter > int(minq)):

                                            break

                                

                                        loopcounter=loopcounter+1

                        json_numbers = json.dumps(slnolist)
                        df=pd.read_csv("csvfiles/"+gtin+".csv")

                        for value in rowIndex:

                                    df.loc[value,'Status']="allocated"

                        df.to_csv("csvfiles/"+gtin+".csv",index=False)
                                
                                
                        # df=pd.read_csv("csvfiles/"+gtin+".csv")
                        # print("start to deleting")
                        # with open("csvfiles/"+gtin+".csv")  as f:
                        #                 readobj=csv.reader(f)
                        #                 counter=-1
                        #                 for row in readobj:
                        #                         if counter<int(minq):
                        #                             df=df.loc[df['Status']=='notallow']
                        #                             df.shape
                        #                             # print("doing") 
                        #                         counter=counter+1
                        # df.to_csv("csvfiles/"+gtin+".csv",index=False)                
                        # print("deleting completed")                                            
                                                                    
                                                        
                                    
                                        
                                            
                                            
                        # gtin=request.data['gtin_number']
                        count=0
                        with open("csvfiles/"+gtin+".csv")  as f:
                            readobj=csv.reader(f)
                            for row in readobj:
                                if(row[3]=="notallow"):
                                    count=count+1
                             
                            print(count)
                                # results = pd.read_csv("csvfiles/"+gtin+".csv")
                                # count=len(results)
                                # print(count)
                            obj = Gtins.objects.get(gtin=gtin)
                            detailObj=Gtins.objects.all().filter(gtin=obj.gtin).update(available_quantity=count)
                                
                            obj = Allocatednumbers.objects.get(batch_number=lot)
                            detailObj=Allocatednumbers.objects.all().filter(batch_number=obj.batch_number).update(available_quantity=count)
                            historysave=History(modelname='Allocated Numbers',           #history table entry
                                    savedid="noid",
                                    operationdone="Allocated Seralnumbers For Batch Number "+lot+" "+"by"+" "+ loginname,
                                    donebyuser=loginname,
                                    donebyuserrole=loginuserrole, 
                                    description="Allocated Seralnumbers For Batch Number "+lot+" "+"by"+" "+ loginname,
                                    donedatetime=datetime.datetime.now())
                            historysave.save()
                            print("history saved")
                            return Response(200) 
                                
                    
                    except:
                        print("except second trty")
                        return Response(500)            
                                        
                                    
                    # return Response(200)
                return Response(serializeobj.errors)
            except:
                print("except")
                return Response(500) 
        
class ProductionOrderReportdate(APIView):  
    def post(self, request):
        # detailsObj = ProdReport.objects.all()
    
        startdate = request.data["datefrom"]
        
        toDate = request.data["dateto"]
        # print(startdate)
        # fromDate=str(request.POST.get('datefrom'))
        # toDate=str(request.POST.get("dateto"))
        # response  =ProductionReport.objects.all().filter(production_date=id)
        
        response=ProdReport.objects.all().filter(production_date__range=(startdate, toDate))
       
        serializeObj = ProdReportSerializer(response, many=True)
        return Response(serializeObj.data)
        
    

    