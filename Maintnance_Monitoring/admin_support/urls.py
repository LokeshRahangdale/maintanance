"""Maintnance_Monitoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from admin_support import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/',admin.site.urls),
    path('a_s_login/',views.ad_support_login,name='a_s_login'),
    path('admin_support/', TemplateView.as_view(template_name='admin_support/admin_support_login.html'), name='admin_support_login'),
    path('home/', TemplateView.as_view(template_name='admin_support/admin_support.html'), name="home"),

    path('add_dept/',views.addDepartment, name="add_dept"),
    path('save_dept/',views.saveDepartment,name='save_dept'),
    path('add_lab/', views.addLab, name="add_lab"),
    path('save_lab/', views.saveLab, name="save_lab"),
    path('add_system/', views.addSystem, name="add_system"),
    path('save_system/',views.saveLab,name="save_system")
]
