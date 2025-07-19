from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from user_auth_app.models import *

# Create your views here.

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user_types = request.POST.get('user_types')

        if user_types == 'Admin':
            CustomUserModel.objects.create_user(
                username=username,
                email=email,
                phone=phone,
                password=phone,
                user_types='Admin',
            )
        else:
            PendingAccountModel.objects.create(
                username=username,
                email=email,
                phone=phone,
                user_types=user_types,
                status = 'Pending'
            )
        return redirect('loginPage')
    return render(request, 'signupPage.html')
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
    return render(request, 'logoutPage.html')

def home(request):
    return render(request, 'home.html')

def pendingAccountList(request):
    pendingAccountData = PendingAccountModel.objects.all()
    return render(request, 'pendingAccountList.html', {'pendingAccount':pendingAccountData})

def acceptPendingAccount(request):
    pendingAccount = PendingAccountModel.objects.all()

    if pendingAccount:
        CustomUserModel.objects.create_user(
            username=pendingAccount.username,
            email=pendingAccount.email,
            password=pendingAccount.phone,
        )
    pendingAccount.delete()
    return redirect('pendingAccountList')