from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics

from sapapp.models import Sapproductionorder,Sapproduct
from sapapp.serializers import SapProductionOrderSerializer,SapProductSerializer
# from masterapp.permissions import ObjectDestroyPermission, Productpermission
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# from masterapp import serializers
class Sapproductionorderview(APIView):
    def get(self, request):
        detailsObj =Sapproductionorder.objects.all()
        serializeObj = SapProductionOrderSerializer(detailsObj, many = True)
        return Response(serializeObj.data)
    
    
class Sapproductionorderviewindividual(APIView):
    def get(self, request, id):
        detailsObj = Sapproductionorder.objects.all().filter(process_order_number=id)
        serializeObj = SapProductionOrderSerializer(detailsObj, many=True)
        return Response(serializeObj.data)    

    
class Sapproductviewindividual(APIView):
    def get(self, request, id):
        detailsObj = Sapproduct.objects.all().filter(gtin_number=id)
        serializeObj = SapProductSerializer(detailsObj, many=True)
        return Response(serializeObj.data) 