from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import AbstractUser

# Create your models here
class Project_artical(models.Model):
    project_artical_id = models.AutoField(primary_key=True)
    project_artical_title = models.CharField(max_length=100)
    project_artical_subheadeing = models.CharField(max_length=200)
    project_artical_body = CKEditor5Field('Text', config_name='extends')
    project_artical_image = models.ImageField(upload_to='images/', default='default.jpg')
    project_artical_date_added = models.DateTimeField(auto_now_add=True)
    project_artical_date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.project_artical_title
    
    def get_absolute_url(self):
        return f'/projects/{self.pk}/'