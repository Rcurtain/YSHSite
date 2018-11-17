from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_list, name="blog_list"),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
]
