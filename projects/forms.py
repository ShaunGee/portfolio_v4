from django import forms
from .models import *
from django_ckeditor_5.widgets import CKEditor5Widget

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project_artical
        fields = ['project_artical_title', 'project_artical_subheadeing', 
                  'project_artical_body', 'project_artical_image']
    
class CreateProjectForm(forms.ModelForm):
    project_artical_body = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    
    class Meta:
        model = Project_artical
        fields = ['project_artical_title', 'project_artical_subheadeing',
                  'project_artical_body', 'project_artical_image']