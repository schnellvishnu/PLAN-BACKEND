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
from accounts.models import History
import datetime

class ManufacturingLocView(APIView):
    def get(self, request):
        detailsObj = ManufacturingLocations.objects.all()
        serializeObj = ManufacturingLocSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

    def post(self, request):
        serializeObj = ManufacturingLocSerializer(data=request.data)
        if serializeObj.is_valid():
            device=serializeObj.save()
            historysave=History( modelname='ManufacturingLocation',
                    savedid=device.id,
                    operationdone='create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Created A New ManufacturingLocation" +"\t" +request.data["name"]+"\t"+"by"+"\t"+ request.data['loggedInUsername'],
                    donedatetime=datetime.datetime.now())
            historysave.save()
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
            
            historysave=History(modelname='ManufacturingLocation',
                                savedid=pk,
                                operationdone='Manufacturing Location of this id Update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Manufacturing Location of id" + request.data["uniqueid"] + "\t"+"Updated",
                                donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteManufacturingLocations(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ManufacturingLocations.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        uniqueid=str(request.data['id'])
        historysave=History(modelname='ManufacturingLocation',
                                savedid=pk,
                                operationdone='Delete',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="Manufacturing Location of id" +"\t" + uniqueid + "\t"+"Deleted",
                                donedatetime=datetime.datetime.now())
        historysave.save()
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
        print("hiiii")
        if serializeObj.is_valid():

            device=serializeObj.save()
            historysave=History( modelname='RegisteredSystem',
                    savedid=device.id,
                    operationdone='create',
                    donebyuser=request.data['loggedInUsername'],
                    donebyuserrole=request.data['loggedInUserrole'], 
                    description="Created A New RegisteredSystem" +"\t" +request.data["system_name"]+"\t"+"by"+"\t"+ request.data['loggedInUsername'],
                    donedatetime=datetime.datetime.now())
            historysave.save()
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
            historysave=History(modelname='RegisteredSystem',
                                savedid=pk,
                                operationdone='RegisteredSystem of this id Update',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="RegisteredSystem of id" + "\t" + request.data["uniqueid"] + "\t"+"Updated",
                                donedatetime=datetime.datetime.now())
            historysave.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteRegisterSystem(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = RegisteredSystem.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        uniqueid=str(request.data['id'])
        historysave=History(modelname='RegisteredSystem',
                                savedid=pk,
                                operationdone='Delete',
                                donebyuser=request.data['loggedInUsername'],
                                donebyuserrole=request.data['loggedInUserrole'],
                                description="RegisteredSystem of id" +"\t" + uniqueid + "\t"+"Deleted",
                                donedatetime=datetime.datetime.now())
        historysave.save()
        detailsObj.delete()
        return Response(200)
class RegisterSystemindividual(APIView):
    def get(self, request, id):
        detailsObj =RegisteredSystem.objects.all().filter(id=id)
        serializeObj = RegisterSystemsSerializer(detailsObj, many=True)
        return Response(serializeObj.data) 
class RegisterSystemIpindividual(APIView):
    def get(self, request, id):
        detailsObj =RegisteredSystem.objects.all().filter(ip_address=id)
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
    
class TrashManufacturinglocation(APIView):
    def delete(self, request, pk):
        try:
            detailsObj =ManufacturingLocations.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = ManufacturingLocations.objects.all().filter(id=pk)
        detailObj=ManufacturingLocations.objects.filter(id=pk).update(manufacturingLocationflag=True)
      
       
        historySave = History(modelname='manufacturinglocations',
                              savedid=pk,
                              operationdone='deletetotrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Deleted the manufacturinglocation " +request.data['name'] +" to trash")
        historySave.save()
        return Response(200)    
    
class RestoreTrashManufacturinglocation(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = ManufacturingLocations.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = ManufacturingLocations.objects.all().filter(id=pk)
        detailObj=ManufacturingLocations.objects.filter(id=pk).update(manufacturingLocationflag=False)
       
       
        historySave = History(modelname='manufacturinglocations',
                              savedid=pk,
                              operationdone='restorefromtrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Restored the manufacturinglocation " +request.data['name'] + " from trash")
        historySave.save()
        return Response(200)    
    
class TrashRegisteredsystem(APIView):
    def delete(self, request, pk):
        try:
            detailsObj =RegisteredSystem.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = RegisteredSystem.objects.all().filter(id=pk)
        detailObj=RegisteredSystem.objects.filter(id=pk).update(productionlineflag=True)
      
       
        historySave = History(modelname='productionline',
                              savedid=pk,
                              operationdone='deletetotrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Deleted the productionline " +request.data['line'] +" to trash")
        historySave.save()
        return Response(200)

class RestoreTrashRegisteredsystem(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = RegisteredSystem.objects.get(pk=pk)
        except:
            return Response("Not found in database")
        detailsObj = RegisteredSystem.objects.all().filter(id=pk)
        detailObj=RegisteredSystem.objects.filter(id=pk).update(productionlineflag=False)
       
       
        historySave = History(modelname='productionline',
                              savedid=pk,
                              operationdone='restorefromtrash',
                              donebyuser=request.data['loggedInUsername'],
                              donebyuserrole=request.data['loggedInUserrole'],
                              donedatetime=datetime.datetime.now(),
                              description="Restored the productionline " +request.data['line'] + " from trash")
        historySave.save()
        return Response(200)
    