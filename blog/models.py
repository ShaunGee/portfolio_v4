from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Blog_artical(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=100)
    blog_subheadeing = models.CharField(max_length=200)
    blog_body = CKEditor5Field('Text', config_name='extends')
    blog_tile_img = models.ImageField(upload_to='blog_images/', default='default.jpg')
    blog_artical_date_added = models.DateTimeField(auto_now_add=True)
    blog_artical_date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.blog_title
    
    def get_absolute_url(self):
        return f'/blogs/{self.pk}/'