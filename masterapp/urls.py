from django.urls import path
from masterapp import views

urlpatterns = [
    path('company/', views.CompanyView.as_view()),
    path('company/update/<int:pk>', views.updateCompany.as_view()),
    path('company/delete/<int:pk>', views.deleteCompany.as_view()),
# __________________________________________________________________
    path('customer/', views.CustomersView.as_view()),
    path('customer/update/<int:pk>', views.updateCustomer.as_view()),
    path('customer/delete/<int:pk>', views.deleteCustomer.as_view()),
    path('customer/<int:id>/',views. CustomerViewIndividual.as_view()),
#----------------------------------------------------------------------
    path('locations/', views.LocationsView.as_view()),
    path('locations/update/<int:pk>', views.updateLocation.as_view()),
    path('locations/delete/<int:pk>', views.deleteLocation.as_view()),
    path('locations/<int:id>/',views.LocationViewIndividual.as_view()),
    #----------------------------------------------------------------------
    path('product/', views.ProductView.as_view()),
    path('product/<int:id>/',views.Productindividual.as_view()),
    path('product/update/<int:pk>', views.updateProduct.as_view()),
    path('product/delete/<int:pk>', views.deleteProduct.as_view()),
    #----------------------------------------------------------------------------
    path('shippo/', views.ShipPOView.as_view()),
    path('shippo/update/<int:pk>', views.updateShipPO.as_view()),
    path('shippo/delete/<int:pk>', views.deleteShipPO.as_view()),
    path('shippo/<int:id>/',views.ShippoViewIndividual.as_view()),
    #-----------------------------------------------------------------------------
    path('productionorder/', views.ProductionOrderView.as_view()),
    path('productionorder/<int:id>/', views.ProductionOrderViewIndividual.as_view()),
    path('productionorder/update/<int:pk>', views.updateProductionOrder.as_view()),
    path('productionorder/delete/<int:pk>', views.deleteProductionOrder.as_view()),
    #-----------------------------------------------------------------------------------
    path('barcodetype/', views.BarCodeTypeView.as_view()),
    path('barcodetype/update/<int:pk>', views.updateBarcodetype.as_view()),
    path('barcodetype/delete/<int:pk>', views.deleteBarcodetype.as_view()),
    #----------------------------------------------------------------------------------
    path('snprovider/', views.SnproviderView.as_view()),
    path('snprovider/update/<int:pk>', views.updateSnprovider.as_view()),
    path('snprovider/delete/<int:pk>', views.deleteSnprovider.as_view()),
    #--------------------------------------------------------------------------------
    path('stock/', views.StockView.as_view()),
    path('stock/update/<int:pk>', views.updateStock.as_view()),
    path('stock/delete/<int:pk>', views.deleteStock.as_view()),
    path('stock/closed', views.Stockclosedview.as_view()),
]