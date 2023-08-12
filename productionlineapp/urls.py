from django.urls import path
from productionlineapp import views

urlpatterns = [
    path('manufacturinglocation/', views.ManufacturingLocView.as_view()),
    path('manufacturinglocation/<int:id>/',views.Manufacturinglocationindividual.as_view()),
    path('manufacturinglocation/update/<int:pk>', views.updateManufacturingLocations.as_view()),
    path('manufacturinglocation/delete/<int:pk>', views.deleteManufacturingLocations.as_view()),
    # ---------------------------------------------------------------------------------------------
    path('registeredsystem/', views.RegisterSystemView.as_view()),
    path('registeredsystem/<int:id>/',views.RegisterSystemindividual.as_view()),
    path('registeredsystem/update/<int:pk>', views.updateRegisterSystem.as_view()),
    path('registeredsystem/delete/<int:pk>', views.deleteRegisterSystem.as_view()),
    #----------------------------------------------------------------------------------------------
    path('task/', views.TaskView.as_view()),
    path('task/update/<int:pk>', views.updateTask.as_view()),
    path('task/delete/<int:pk>', views.deleteTask.as_view()),
]