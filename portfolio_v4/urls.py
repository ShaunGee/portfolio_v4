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
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.about, name='about'),
    path('blogs/', views.Blogs.as_view(), name='blogs'),
    path('projects/', views.Projects.as_view(), name='projects'),
    
    path('mainframe/projects/', include('projects.urls', namespace='projects')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('mainframe/', views.backend_dashboard, name='mainframe'),
    path('mainframe/blogs/', include('blog.urls', namespace='blogs')),
   
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='projectDetailView'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blogDetailView'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)