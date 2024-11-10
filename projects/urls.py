"""
URL configuration for portfolio_v4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from portfolio_v4 import settings
from django.conf.urls.static import static

app_name = 'projects'

urlpatterns = [
    path('', views.Project_landing_page.as_view(), name='projects_landing_page'),
    path('create/',views.Create_Project.as_view(), name='projects_create_form'),
    path('<int:pk>/',views.Display_Project_Artical.as_view(), name='BackEndProjectDetailView'),
    path('<int:pk>/edit',views.Edit_Project_Artical.as_view(), name='project_artical_edit_view'),
    path('<int:pk>/delete', views.DeleteArtical.as_view(), name='project_artical_delete_view'),
    
    
]
