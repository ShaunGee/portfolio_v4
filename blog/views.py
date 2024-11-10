from django.views import View
from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from .forms import CreateBlogForm
from .models import Blog_artical
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView


# Create your views here.


class BlogsDashboard(LoginRequiredMixin, View):
    def get(self,request):
        model = Blog_artical.objects.all()
        return (render(request, "blogs/backend_blogs_dashboard.html", 
                       {'blogs':model,
                        'view_type':'blogs',
                        'access' : 'back_end',
                        }))
    

class CreateBlog(LoginRequiredMixin, View):
    
    def post(self, request):
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs_dashboard')
        return redirect('https://www.google.com')
    
    
    def get(self, request):
        form = CreateBlogForm
        return(render(request, 'blogs/blog_create_form_page.html', {'form':form}))
    
    
class Display_Artical(LoginRequiredMixin, DetailView):
    model = Blog_artical
    context_object_name = 'blog_artical'
    template_name = 'blogs/backend_blog_artical_detail_view.html'
    
class Edit_Blog_Artical(LoginRequiredMixin, UpdateView):
    model = Blog_artical
    template_name = 'blogs/update_blog_artical.html'
    fields = '__all__'
    context_object_name = 'sdfs'


class DeleteArtical(View):
    def post(self, request, pk):
        delObj = get_object_or_404(Blog_artical, pk=pk)
        delObj.delete()
        return JsonResponse({'success': True})