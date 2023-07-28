from django.shortcuts import render,redirect
from blog.models import blog
from django.contrib.auth.models import User #user model
from .forms import blogForm
from .models import category
# Create your views here.
def home(request):
    blogs = blog.objects.all()
    form = blogForm()
    context = {
        'blogs' : blogs,
        'form' : form,
    }
    return render(request,'blog/home.html',context)

def add_blog(request):
    if request.method == "POST":
        # id = request.POST.get("category")
        # c = category.objects.get(id=id)
        # title = request.POST.get("title")
        # description = request.POST.get("description")
        # image = request.POST.get("image")
        # b = blog(
        #     category = c,
        #     title = title,
        #     author = request.user,
        #     description = description,
        #     image = image
        # )
        # b.save()
        f = blogForm(request.POST,request.FILES)
        f=f.save(commit=False)
        f.author = request.user
        print(f)
        f.save()
    return redirect('home')

def blog_details(request,id):
    bg = blog.objects.get(id=id) 
    context = {
        'blog' : bg,
    }
    return render(request,'blog/blog.html',context)

