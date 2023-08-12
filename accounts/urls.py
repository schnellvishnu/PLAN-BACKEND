from django.urls import path
from accounts import views


urlpatterns = [
    path('userrole/', views.UserroleView.as_view()),
    path('userrole/update/<int:pk>', views.updateUserrole.as_view()),
    path('userrole/delete/<int:pk>', views.deleteUserrole.as_view()),
    #___________________________________________________________________________
    path('history/', views.AuditLogView.as_view()),
    # path('auditlog/update/<int:pk>', views.updateAuditlog.as_view()),
    path('history/delete/<int:pk>', views.deleteAuditlog.as_view()),
   
    path('historymodel/<id>/', views.HistoryemployeandmodelIndividual.as_view()),
    path('historymodelname/<id>/', views.HistoryemployeandmodelnameIndividual.as_view()),

    #____________________________________________________________________________
    path('register/',views.RegisterView.as_view()),
    path('update/<int:pk>', views.updateRegister.as_view()),
    path('delete/<int:pk>', views.deleteRegister.as_view()),
    path('userAuthVerify', views.userAuthVerify.as_view()),
    path('register/<int:id>/',views.Registerindividual.as_view()),
    path('logInController', views.logInController.as_view()),
    path('profile/<id>/', views.RegisteremployeIndividual.as_view()),
    path('logoutController', views.logoutController.as_view()),
    
     path('userAuditReportdate/', views.UserAuditReportdate.as_view()),
    #____________________________________________________________________________
    # path('reg/', views.RegView.as_view()),
    # path('reg/update/<int:pk>', views.updateReg.as_view()),
    # path('reg/delete/<int:pk>', views.deleteReg.as_view()),
    path('userPermissionEdit/', views.userPermissionEdit.as_view()),
    path('userrolePermissionsRead', views.UserrolePermissionsRead.as_view()),
]