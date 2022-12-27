from accounts.models import UserRole,History,Register
from rest_framework import serializers
from django.contrib.auth.models import User
class UserRoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =UserRole
        fields = "__all__"
class HistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model =History
        fields = "__all__"
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Register
        fields = "__all__"
# class RegSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model =Reg
#         fields = "__all__"


