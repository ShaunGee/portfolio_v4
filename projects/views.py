from django.shortcuts import render

# Create your views here.

#this page is the landing. It contains a galary of projects
def projects_landing_page(request):
    return render(request, 'projects_landing_page.html')

