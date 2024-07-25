from django import views
from django.shortcuts import render, redirect
from .forms import CreateBlogForm
from .models import Blog_artical

# Create your views here.

class BlogsDashboard(views.View):
    def get(self,request):
        model = Blog_artical.objects.all()
        return (render(request, "blogs/backend_blogs_dashboard.html", {'model':model}))
    
    
class CreateBlog(views.View):
    
    def post(self, request):
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs_dashboard')
        return redirect('https://www.google.com')
    
    
    def get(self, request):
        form = CreateBlogForm
        return(render(request, 'blogs/blog_create_form_page.html', {'form':form}))