from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from . import webapps
from django.views.generic import TemplateView, DetailView
from projects.models import Project_artical
from blog.models import Blog_artical

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'frontend/about.html')



def contact(request):
    return render(request, 'frontend/contact.html')



def login(request):
    return render(request, 'login.html')

@login_required
def backend_dashboard(request):
    context = {
        'apps': webapps.currentWorkingApps
    }
    
    return render(request, 'backend_dashboard.html', context)

class HomePage(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['projects'] = Project_artical.objects.order_by('-project_artical_date_added')[:2]
        context['blogs'] = Blog_artical.objects.order_by('-blog_artical_date_added')[:2]
        return context


class Projects(TemplateView):
    template_name = 'frontend_projects_landing_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = 'projects'
        context['projects'] = Project_artical.objects.all()
        return context
    

class Blogs(TemplateView):
    template_name = 'frontend_blogs_landing_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_type'] = 'blogs'
        context['blogs'] = Blog_artical.objects.all()
        return context
    
class ProjectDetailView(DetailView):
    template_name = 'frontend_artical_page_base.html'
    model = Project_artical
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artical_type"] = 'project'
        return context
    
    
class BlogDetailView(DetailView):
    template_name = 'frontend_artical_page_base.html'
    model = Blog_artical
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artical_type"] = 'blog'
        return context