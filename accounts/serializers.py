from accounts.models import UserRole,History,Register,UserrolePermissions,UserAuditHistoryOnly
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


class UserrolePermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserrolePermissions
        fields="__all__"

class UserHistorySerializer(serializers.ModelSerializer):
                        
    class Meta:
        model =UserAuditHistoryOnly
        fields = "__all__"
