from django import forms
from .models import *

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project_artical
        fields = ['project_artical_title', 'project_artical_subheadeing', 'project_artical_body', 'project_artical_image']
    
class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project_artical
        fields = ['project_artical_title', 'project_artical_subheadeing', 'project_artical_body', 'project_artical_image']