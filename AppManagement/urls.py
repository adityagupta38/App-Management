"""AppManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Apps import views
from AppManagement import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authviews
from Apps import userviews
from rest_framework import routers
from Apps import apiviews


router = routers.DefaultRouter()
router.register('apps', apiviews.AppsApi, basename='apps')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api_auth/', include('rest_framework.urls')),
    path('',include(router.urls)),
    path('adminlogin/', views.admin_login, name='admin_login'),
    path('admin_register/', views.admin_register, name='admin_register'),
    path('adminhome<int:pk>/', views.admin_home, name='admin_home'),
    path('addapp<int:pk>', views.add_app, name='add_app'),
    path('deleteapp<int:pk>/', views.app_delete, name='delete_app'),
    path('adminlogout/', views.admin_logout, name='admin_logout'),
    path('userlogin/', authviews.LoginView.as_view(next_page='/userhome/', template_name='user_login.html'), name='user_login'),
    path('usersignup', userviews.user_signup, name='user_signup'),
    path('userhome/', userviews.user_home, name='user_home'),
    path('userprofile/', userviews.userprofile, name='user_profile'),
    path('userlogout/', authviews.LogoutView.as_view(next_page='/userlogin/'), name='user_logout'),
    path('userappdetail<int:pk>', userviews.user_app_detail, name='user_app_detail'),
    path('userpoints/', userviews.userpoints, name='user_points'),
    path('usertasks/', userviews.usertask, name='user_tasks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
