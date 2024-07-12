from django.shortcuts import render
from django.views import View
from .models import *
from . import forms

# Create your views here.

#this page is the landing. It contains a galary of projects



class Project_landing_page(View):
    
    def get(self,request):
        form = forms.ProjectsForm()
        return render(request, 'projects_landing_page.html', {'projectForm':form})
    
    