from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogify_home,name='blogify_home')
]
