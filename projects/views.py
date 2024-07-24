from django.shortcuts import render, redirect
from django.views import View
from .models import *
from . import forms

# Create your views here.

#this page is the landing. It contains a galary of projects



class Project_landing_page(View):
    template_name = 'projects/landingpage.html'
    
    
    def get(self,request):
        form = forms.ProjectsForm()
        return render(request, 'projects/projects_landing_page.html', {'projectForm':form})
    


class Create_Project(View):
    
    def post(self, request):       
        form = forms.CreateProjectForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("projects:projects_landing_page")
        return redirect('https://www.google.com')

    def get(self, request):
        form = forms.CreateProjectForm()
        return render(request, 'projects/projects_create_form_page.html', {'form': form})
    