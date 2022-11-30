from django.shortcuts import render
from rest_framework import generics

from accounts.models import  UserRole,AuditLog,Register
from accounts.serializers import UserRoleSerializer,AuditLogSerializer,RegisterSerializer
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
        detailsObj = AuditLog.objects.all()
        serializeObj = AuditLogSerializer(detailsObj, many = True)
        return Response(serializeObj.data)

   
    def post(self, request):
        serializeObj = AuditLogSerializer(data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class updateAuditlog(APIView):
    def put(self, request, pk):
        try:
            detailObj = AuditLog.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        serializeObj = AuditLogSerializer(detailObj, data=request.data)
        if serializeObj.is_valid():
            serializeObj.save()
            return Response(200)
        return Response(serializeObj.errors)

class deleteAuditlog(APIView):
    def delete(self, request, pk):
        try:
            detailsObj = AuditLog.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)
#----------------------------------------------------------



class RegisterView(APIView):

    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        detailsObj = Register.objects.all()
        serializeObj =RegisterSerializer(detailsObj, many = True)
        return Response(serializeObj.data)


    def post(self, request):
            serializeObj = RegisterSerializer(data=request.data)
            if serializeObj.is_valid():
                serializeObj.save()

    #             ##########  Registering the user in User model
                userMail = request.data['email']
                userName = request.data['Name']
                userPassword = 'password'
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
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
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
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            detailsObj = Register.objects.get(pk=pk)
        except:
            return Response("Not found in database")

        detailsObj.delete()
        return Response(200)

class userAuthVerify(APIView):

	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	def post(self, request):
		userData = Register.objects.filter(email=request.data['username']).values()
		return Response(userData[0]['userRole'])

	# def post(self, request):
	# 	return Response(201)

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
