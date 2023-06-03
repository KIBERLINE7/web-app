from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('employee/', views.employee, name='employee'),
    path('supervisor/', views.supervision, name='supervisor'),
    path('user_update/', views.UserUpdates, name='userupdates'),
    #path('recoverypass/'),
    path('edit_user/<int:pk>', views.EditUser, name='edituser'),
    path('editpassword/', views.EditPassword, name='edidpass'),
    path('logout', views.logout, name='logout'),
    #path('distributor', views.distributor, name='distributor'),
     path('viewprofile/<int:pk>', views.viewprofile, name='viewprofile'),
    #path('test/', views.Test)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)