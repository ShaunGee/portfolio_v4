from django import views
from django.shortcuts import render

# Create your views here.

class BlogsDashboard(views.View):
    def get(self,request):
        return (render(request, "blogs/backend_blogs_dashboard.html"))