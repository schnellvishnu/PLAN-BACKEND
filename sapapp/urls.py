from django.urls import path
from sapapp import views

urlpatterns = [
  path('sapproductionorder/',views.Sapproductionorderview.as_view()),
  path('sapproductionorder/<int:id>/',views.Sapproductionorderviewindividual.as_view()),
  path('sapproduct/<int:id>/',views.Sapproductviewindividual.as_view()),
  # path('productionorder/update/<int:pk>', views.updateProductionOrder.as_view()),
  # path('productionorder/delete/<int:pk>', views.deleteProductionOrder.as_view()),
]