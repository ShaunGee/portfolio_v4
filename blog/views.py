from django import views
from django.shortcuts import render, redirect
from .forms import CreateBlogForm

# Create your views here.

class BlogsDashboard(views.View):
    def get(self,request):
        return (render(request, "blogs/backend_blogs_dashboard.html"))
    
    
class CreateBlog(views.View):
    
    def post(self, request):
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs_dashboard')
        return redirect('https://www.google.com')
    
    
    def get(self, request):
        form = CreateBlogForm
        return(render(request, 'blogs/blog_create_form_page.html', {'form':form}))