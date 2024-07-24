from django import forms
from .models import *
from django_ckeditor_5.widgets import CKEditor5Widget
        
class CreateBlogForm(forms.ModelForm):
    blog_body = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
    
    class Meta:
        model = Blog_artical
        fields = [
            'blog_id',
            'blog_title',
            'blog_subheadeing',
            'blog_body'
        ]