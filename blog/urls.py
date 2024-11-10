from django.urls import path

from .views import *

app_name = 'blogs'

urlpatterns =[
    path("", BlogsDashboard.as_view() , name='blogs_dashboard'),
    path("create/", CreateBlog.as_view(), name='blogs_create_form'),
    path('<int:pk>/',Display_Artical.as_view(), name='BackEndBlogDetailView'),
    path('<int:pk>/edit',Edit_Blog_Artical.as_view(), name='edit_display_artical'),
    path('<int:pk>/delete', DeleteArtical.as_view(), name='blog_artical_delete_view'),
]