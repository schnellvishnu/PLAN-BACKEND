from django.contrib import admin
from accounts.models import UserRole,AuditLog,Register,History
# Register your models here.
admin.site.register(UserRole)
admin.site.register(AuditLog)
# admin.site.register(Reg)
admin.site.register(Register)
admin.site.register(History)
