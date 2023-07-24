from django.shortcuts import render

# Create your views here.
def blogify_home(request):
    return render(request,'about/blogify.html')