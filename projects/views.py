from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from .models import *
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#this page is the landing. It contains a galary of projects



class Project_landing_page(LoginRequiredMixin, View):
    template_name = 'projects/projects_landing_page.html'

    def get(self,request):
        model = Project_artical.objects.all()
        form = forms.ProjectsForm()
        return render(request, self.template_name, 
                      {'projectForm':form,
                       'projects':model,
                       'view_type': 'projects',
                       'access' : 'back_end',
                       })
    


class Create_Project(LoginRequiredMixin, View):
    
    def post(self, request):       
        form = forms.CreateProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect("projects:projects_landing_page")
        return redirect('https://www.google.com')

    def get(self, request):
        form = forms.CreateProjectForm()
        return render(request, 'projects/projects_create_form_page.html', {'form': form})
    
 
class Display_Project_Artical(LoginRequiredMixin, DetailView):
    model = Project_artical
    template_name = 'backend_artical_page_base.html'
    context_object_name = 'project'
    

     
class Edit_Project_Artical(LoginRequiredMixin, UpdateView):
    model = Project_artical
    fields='__all__'
    template_name = 'projects/edit_project_artical.html'
    context_object_name = 'artical_form'
    


class Home_Page_Project_View(View):
    def get_queryset(self):
        q = Project_artical.objects.order_by('-date_added')[:2]
        return q
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        context = {
            'project_articals_homepage':queryset,
        }
        return render(request, template_name='test.html', context = context)
    
class FrontendDetailView(DetailView):
        model = Project_artical
        
class DeleteArtical(View):
    def post(self, request, pk):
        print('shaun')
        print(pk)
        delObj = get_object_or_404(Project_artical, pk=pk)
        delObj.delete()
        return JsonResponse({'success': True})
    
    