from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from . import webapps

def index(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')

@login_required
def backend_dashboard(request):
    context = {
        'apps': webapps.currentWorkingApps
    }
    
    return render(request, 'backend_dashboard.html', context)

