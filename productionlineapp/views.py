from django.shortcuts import render
from rest_framework import generics

from productionlineapp.models import ManufacturingLocations,RegisteredSystem, Task
from productionlineapp.serializers import ManufacturingLocSerializer,RegisterSystemsSerializer,TaskSerializer
# from masterapp.permissions import ObjectDestroyPermission, Productpermission
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from productionlineapp import serializers
# from django_filters.rest_framework import  DjangoFilterBackend
# from apps_extra_code.custom_list_search_filter import CustomSearchFilter



class ManufacturingLocView(APIView):
    def get(self, request):
        detailsObj = ManufacturingLocations.objects.all()
        serializeObj = ManufacturingLocSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

    def post(self, request):
        serializeObj = ManufacturingLocSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateManufacturingLocations(APIView):
    def put(self, request, pk):
        try:
            detailObj = ManufacturingLocations.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = ManufacturingLocSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteManufacturingLocations(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ManufacturingLocations.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
class  Manufacturinglocationindividual(APIView):
    def get(self, request, id):
        detailsObj =ManufacturingLocations.objects.all().filter(id=id)
        serializeObj = ManufacturingLocSerializer(detailsObj, many=True)
        return Response(serializeObj.data) 
# --------------------------------------------------------------------

# registerd system

class RegisterSystemView(APIView):
    def get(self, request):
        detailsObj = RegisteredSystem.objects.all()
        serializeObj = RegisterSystemsSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

    def post(self,request):
        serializeObj = RegisterSystemsSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateRegisterSystem(APIView):
    def put(self, request, pk):
        try:
            detailObj = RegisteredSystem.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = RegisterSystemsSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteRegisterSystem(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = RegisteredSystem.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
class RegisterSystemindividual(APIView):
    def get(self, request, id):
        detailsObj =RegisteredSystem.objects.all().filter(id=id)
        serializeObj = RegisterSystemsSerializer(detailsObj, many=True)
        return Response(serializeObj.data) 
#----------------------------------------------------------

class TaskView(APIView):
    def get(self, request):
        detailsObj = Task.objects.all()
        serializeObj = TaskSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

    def post(self,request):
        serializeObj = TaskSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateTask(APIView):
    def put(self, request, pk):
        try:
            detailObj = Task.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = TaskSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteTask(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = Task.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)