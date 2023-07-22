from django.urls import path
from blog import views

urlpatterns = [
    path("",views.home,name="home"),
    path("<int:id>",views.blog_details,name="blog_details"),
    path("add_blog",views.add_blog,name='add_blog')
]