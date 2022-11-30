from django.urls import path
from accounts import views


urlpatterns = [
    path('userrole/', views.UserroleView.as_view()),
    path('userrole/update/<int:pk>', views.updateUserrole.as_view()),
    path('userrole/delete/<int:pk>', views.deleteUserrole.as_view()),
    #___________________________________________________________________
    path('auditlog/', views.AuditLogView.as_view()),
    path('auditlog/update/<int:pk>', views.updateAuditlog.as_view()),
    path('auditlog/delete/<int:pk>', views.deleteAuditlog.as_view()),
    #____________________________________________________________________________
    path('register/', views.RegisterView.as_view()),
    path('update/<int:pk>', views.updateRegister.as_view()),
    path('delete/<int:pk>', views.deleteRegister.as_view()),
    path('userAuthVerify', views.userAuthVerify.as_view())
    #_______________________________________________________________________
    # path('reg/', views.RegView.as_view()),
    # path('reg/update/<int:pk>', views.updateReg.as_view()),
    # path('reg/delete/<int:pk>', views.deleteReg.as_view()),


]