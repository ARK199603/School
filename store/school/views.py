from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"Passwords not match")
            return redirect('register')
    return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

        else:
            messages.info(request, "invalid")
            return redirect('login')
        return redirect('form')

    return render(request, 'login.html')


def form(request):
    if request.method=="POST":
        messages.info(request, "Suceess")

    return render(request,'form.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
