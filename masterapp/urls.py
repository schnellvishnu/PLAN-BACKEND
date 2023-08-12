from django.urls import path
from masterapp import views

urlpatterns = [
    path('company/', views.CompanyView.as_view()),
    path('company/<int:id>/',views.Companyindividual.as_view()),
    path('company/update/<int:pk>', views.updateCompany.as_view()),
    path('company/delete/<int:pk>', views.deleteCompany.as_view()),
#---------------------------------------------------------------------------------------
    path('companyerp/', views.CompanyErpView.as_view()),
    path('companyerp/<int:id>/',views.CompanyErpindividual.as_view()),
    path('companyerp/update/<int:pk>', views.updateCompanyErp.as_view()),
    #///////////////////////////////////////////////////////////////////////////////////
    path('companyproperty/', views.CompanyPropertyView.as_view()),
    path('companyproperty/<int:id>/',views.CompanyPropertyindividual.as_view()),
    path('companyproperty/update/<int:pk>', views.updateCompanyProperty.as_view()),
# ......................................................................................
    path('tracelink/',views.Tracelinkview.as_view()),
    path('tracelink/update/<int:pk>',views.updateTracelink.as_view()),
    path('tracelink/<int:id>/',views.Tracelinkviewindividual.as_view()),
# ________________________________________________________________________________________
    path('customertracelink/', views.CustomersTracelinkView.as_view()),
    path('customertracelink/update/<int:pk>', views.updateCustomerTracelink.as_view()),
    path('customertracelink/<int:id>/',views. CustomerTracelinkViewIndividual.as_view()), 
#------------------------------------------------------------------------------------------
    path('customer/', views.CustomersView.as_view()),
    path('customer/update/<int:pk>', views.updateCustomer.as_view()),
    path('customer/delete/<int:pk>', views.deleteCustomer.as_view()),
    path('customer/<int:id>/',views. CustomerViewIndividual.as_view()),
     
# ----------------------------------------------------------------------------------
    path('customerproperty/',views.CustomerPropertyview.as_view()),
    path('customerproperty/update/<int:pk>',views.updateCustomerProperty.as_view()),
    path('customerproperty/<int:id>/',views.CustomerPropertyViewIndividual.as_view()),
#-------------------------------------------------------------------------------------------
    path('locations/', views.LocationsView.as_view()),
    path('locations/update/<int:pk>', views.updateLocation.as_view()),
    path('locations/delete/<int:pk>', views.deleteLocation.as_view()),
    path('locations/<int:id>/',views.LocationViewIndividual.as_view()), 
#--------------------------------------------------------------------------------------------   
    path('locationproperty/',views.LocationPropertyview.as_view()),
    path('locationproperty/update/<int:pk>',views.updateLocationProperty.as_view()),
    path('locationproperty/<int:id>/',views.LocationPropertyViewIndividual.as_view()),
#-------------------------------------------------------------------------------------------
    path('product/', views.ProductView.as_view()),
    path('product/<int:id>/',views.Productindividual.as_view()),
    path('product/update/<int:pk>', views.updateProduct.as_view()),
    path('product/delete/<int:pk>', views.deleteProduct.as_view()),
 #------------------------------------------------------------------------------------------   
    path('producterp/',views.ProductErpview.as_view()),
    path('producterp/update/<int:pk>',views.UpdateProductErp.as_view()),
    path('producterp/<int:id>/',views.ProductErpIndividual.as_view()), 
 #------------------------------------------------------------------------------------------   
    path('productproperty/', views.ProductPropertyView.as_view()),
    path('productproperty/<int:id>/',views.ProductindividualProperty.as_view()),
    path('productproperty/update/<int:pk>', views.updateProductProperty.as_view()),
    path('productproperty/delete/<int:pk>', views.deleteProductProperty.as_view()),
#-------------------------------------------------------------------------------------------   
    path('producthrf/', views.ProducthrfView.as_view()),
    path('producthrf/<int:id>/',views.Productindividualhrf.as_view()),
    path('producthrf/update/<int:pk>', views.updateProducthr.as_view()),
#------------------------------------------------------------------------------------------- 
    path('productmarket/', views.ProductMarketview.as_view()),
    path('productmarket/<int:id>/',views.ProductmarketIndividual.as_view()),
    path('productmarket/update/<int:pk>',views.UpdateProductmarket.as_view()),  
#--------------------------------------------------------------------------------------------
    path('shippo/', views.ShipPOView.as_view()),
    path('shippo/update/<int:pk>', views.updateShipPO.as_view()),
    path('shippo/delete/<int:pk>', views.deleteShipPO.as_view()),
    path('shippo/<int:id>/',views.ShippoViewIndividual.as_view()),
    path('shippoint/', views.ShipPOViewget.as_view()),
    path('shippoint/<int:id>/',views.ShippoProductionordernumberGetingIndividual.as_view()),
    
    
      
#--------------------------------------------------------------------------------------------   
    path('shippoproperty/', views.ShipPoPropertyView.as_view()),
    path('shippoproperty/update/<int:pk>', views.updateShipPoProperty.as_view()),
    path('shippoproperty/delete/<int:pk>', views.deleteShipPoProperty.as_view()),
    path('shippoproperty/<int:id>/',views.ShipPoindividualProperty.as_view()),
    
    path('ShippoauditReportdate/', views.ShippoAuditReportdate.as_view()),
#--------------------------------------------------------------------------------------------
    path('productionorder/', views.ProductionOrderView.as_view()),
    path('productionorder/<int:id>/', views.ProductionOrderViewIndividual.as_view()),
    path('productionorderreport/<id>/', views.ProductionOrderReportIndividual.as_view()),
    path('productionorder/update/<int:pk>', views.updateProductionOrder.as_view()),
    path('productionorder/delete/<int:pk>', views.deleteProductionOrder.as_view()),  
#--------------------------------------------------------------------------------------------   
    path('poproperty/', views.PoProperty.as_view()),
    path('poproperty/<int:id>/', views.PoPropertyindividual.as_view()),
    path('poproperty/update/<int:pk>', views.updatePoProperty.as_view()),
    path('poproperty/delete/<int:pk>', views.deleteProductionOrder.as_view()),  
#--------------------------------------------------------------------------------------------    
    path('productionorderhrf/', views.ProductionorderhrfView.as_view()),
    path('productionorderhrf/<int:id>/',views.Productionorderindividualhrf.as_view()),
    path('productionorderhrf/update/<int:pk>', views.updateProductionorderhrfView.as_view()),
    # path('hrfjson/',views.Hrfjsonview.as_view()),
    # path('hrfjson/update/<int:pk>', views.updateProducthrf.as_view()), 
#--------------------------------------------------------------------------------------------
    path('barcodetype/', views.BarCodeTypeView.as_view()),
    path('barcodetype/update/<int:pk>', views.updateBarcodetype.as_view()),
    path('barcodetype/delete/<int:pk>', views.deleteBarcodetype.as_view()),
    path('barcodetype/<int:id>/',views.Barcodeindividual.as_view()),
#-------------------------------------------------------------------------------------
    path('snprovider/', views.SnproviderView.as_view()),
    path('snprovider/update/<int:pk>', views.updateSnprovider.as_view()),
    path('snprovider/delete/<int:pk>', views.deleteSnprovider.as_view()),
#-------------------------------------------------------------------------------------
    path('stock/', views.StockView.as_view()),
    path('stock/update/<int:pk>', views.updateStock.as_view()),
    path('stock/delete/<int:pk>', views.deleteStock.as_view()),
    path('stock/closed', views.Stockclosedview.as_view()),
# -------------------------------------------------------------------------------------
    path('tracelink/',views.Tracelinkview.as_view()),
    path('tracelink/update/<int:pk>',views.updateTracelink.as_view()),
    path('tracelink/<int:id>/',views.Tracelinkviewindividual.as_view()),
# ------------------------------------------------------------------------------------
    # path('erpsettings/',views.Erpview.as_view()),
    # path('erp/update/<int:pk>',views.updateErpview.as_view()),  
    path('markets/',views.Marketsview.as_view()),
    path('markets/delete/<int:pk>',views.deleteMarket.as_view()),
# -----------------------------------------------------------------------------------
    path('gtin/', views.Gtinview.as_view()),
    path('gtin/update/<int:pk>', views.updateGtinview.as_view()),
    path('gtin/delete/<int:pk>', views.deleteGtinview.as_view()),
    path('gtin/<int:id>/',views.Gtinindividualview.as_view()),
#------------------------------------------------------------------------------------   
    path('printer/', views.printerview.as_view()),
    path('printer/update/<int:pk>', views.updatePrinterview.as_view()),
    path('printer/delete/<int:pk>', views.deletePrinterview.as_view()),
    path('printer/<int:id>/',views.Printerindividualview.as_view()),
    
    path('hrfdata/<int:id>/',views.Hrfdata.as_view()),
    
    path('downloadcodes/', views.Downloadcodesget.as_view()),
    path('downloadcodes/<int:id>/',views.Downloadindividualview.as_view()),
    #  path('downloadcodesprocessno/<int:id>/',views.Downloadcodesview.as_view()),
    
    path('xmldata/', views.Xmldataindividual.as_view()),
    path('commissioningxmldata/', views.Commissioningxml.as_view()),
    path('destroyxmldata/', views.Destroyingxml.as_view()),
    
    path('uploadxml/', views.Uploadcommissioningxml.as_view()),
    path('uploadshipmentxml/', views.Uploadshipmentxml.as_view()),
    path('uploaddestroyxml/', views.UploadDestroyxml.as_view()),
    
    path('downloadshipmentxml/', views.Downloadshipmentxml.as_view()),
    path('downloadcommissioningxml/', views.Downloadcommissioningxml.as_view()),
    path('downloaddestroyxml/', views.Downloaddestroyxml.as_view()),
    
    path('downloadallxml/', views.Downloadallxmlfiles.as_view()),
    
]