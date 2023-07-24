from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('passsword')
        user_exists = False
        if User.objects.filter(username=username).exists():
            # print('username is already taken')
            messages.error(request, "Username is already taken, try with a new one")
            user_exists = True
        if User.objects.filter(email=email).exists():
            # print('email is already taken')
            messages.error(request, "Email is already taken, try with a new one")
            user_exists = True
        if user_exists:
            return render(request,'user/signup.html')
        user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                password = password
        )
        user.save()
        messages.success(request,"Account created successfully.")
    return render(request,'user/signup.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is None:
                messages.error(request,"Invalid username or password")
                return render(request,'user/signin.html')
        else:
                login(request,user)
                return redirect("home")
    return render(request,'user/signin.html')

def signout(request):
    logout(request)
    return render(request,'user/signin.html')

def profile(request):
     return render(request,'user/profile.html')