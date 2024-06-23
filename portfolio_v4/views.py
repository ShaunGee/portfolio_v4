from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView

def index(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


class MainFrameLoginView(LoginView):
    template_name = 'login.html'

