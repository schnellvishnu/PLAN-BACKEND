from django.urls import path
from reportapp import views

urlpatterns = [
    path('ProductionOrderReport/', views.ProductionOrderReport.as_view()),
    path('ProductionOrderReport/<id>/', views.ProductionOrderReportIndividual.as_view()),
    path('ProductionOrderReportdate/', views.ProductionOrderReportdate.as_view()),
    path('mysyip/', views.Printeripview.as_view()),
    # path('ProductionOrderReportdate/<id>/', views.ProductionOrderReportdate.as_view()),
]