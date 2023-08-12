from django.contrib import admin
from masterapp.models import Company,Customers,BarCodeType,SnProvider,Stock,Locations,ShipPO,Product,ProductionOrder,Gtins,PrinterdataTable,Downloadcodes
# Register your models here.
admin.site.register(Company)
admin.site.register(Customers)
admin.site.register(Locations)
admin.site.register(Product)
admin.site.register(ShipPO)
admin.site.register(ProductionOrder)
admin.site.register(BarCodeType)
admin.site.register(SnProvider)
admin.site.register(Stock)
admin.site.register(Gtins)
admin.site.register(PrinterdataTable)
admin.site.register(Downloadcodes)
# admin.site.register(Tracelinksettings)
# admin.site.register(Erpsetting)