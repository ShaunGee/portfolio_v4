from django.urls import path

from .views import *

app_name = 'blogs'

urlpatterns =[
    path("", BlogsDashboard.as_view() , name='blogs_dashboard'),
    path("create/", CreateBlog.as_view(), name='blogs_create_form'),
]