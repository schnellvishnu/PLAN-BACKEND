from django.contrib import admin
from .models import Sapcustomers,Saplocations,SapmanufacturingLocations,Sapproduct,Sapproductionorder,SapregisteredSystem
# Register your models here.
admin.site.register(Sapcustomers)
admin.site.register(Saplocations)
admin.site.register(SapmanufacturingLocations)
admin.site.register(Sapproduct)
admin.site.register(Sapproductionorder)
admin.site.register(SapregisteredSystem)