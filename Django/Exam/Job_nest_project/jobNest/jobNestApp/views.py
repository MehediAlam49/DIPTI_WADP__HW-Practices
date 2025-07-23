from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.hashers import check_password
from jobNestApp.models import *

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')

        if password== confirm_password:
            CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=confirm_password,
                user_type=user_type,
            )

            return redirect('loginPage')
    return render(request, 'registerPage.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'loginPage.html')
def logoutPage(request):
    return redirect('loginPage')
def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')