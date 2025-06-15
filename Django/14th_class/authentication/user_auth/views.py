from django.shortcuts import render, redirect
from user_auth.models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    if request.method =="POST":
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            userInfo = userAuthModel(
                fullname = fullname,
                username = username,
                email = email,
                contact = contact,
            )
            userInfo.save()
            return redirect('login')
        else:
            print("-------password doesn't match")
    return render(request, 'login.html')