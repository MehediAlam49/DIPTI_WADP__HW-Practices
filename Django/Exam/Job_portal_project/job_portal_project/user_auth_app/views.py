from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

from user_auth_app.models import *
from employer_app.models import *
from candidate_app.models import *

# Create your views here.

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user_type = request.POST.get('user_type')

        if user_type == 'Admin':
            CustomUserModel.objects.create_user(
                username=username,
                email=email,
                phone=phone,
                password=phone,
                user_type='Admin',
            )
        else:
            PendingAccountModel.objects.create(
                username=username,
                email=email,
                phone=phone,
                user_type=user_type,
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
    logout(request)
    return redirect('loginPage')

def home(request):
    jobData = JobModel.objects.all()
    return render(request, 'home.html',{'jobData':jobData})
def profile(request):
    return render(request, 'profile.html')

def pendingAccountList(request):
    pendingAccountData = PendingAccountModel.objects.all()
    return render(request, 'pendingAccountList.html', {'pendingAccount':pendingAccountData})

def acceptPendingAccount(request, id):
    accountData = PendingAccountModel.objects.get(id=id)
    if accountData:
        userData = CustomUserModel.objects.create_user(
            username=accountData.username,
            email=accountData.email,
            password=accountData.phone,
            user_type=accountData.user_type,
            phone=accountData.phone,
        )
        if userData:
            if accountData.user_type == 'Employer':
                EmployerProfileModel.objects.create(
                    employer_user=userData,
                    email=accountData.email,
                    phone=accountData.phone,
                )
            elif accountData.user_type == 'Candidate':
                CandidateProfileModel.objects.create(
                    candidate_user=userData,
                    email=accountData.email,
                    phone=accountData.phone,
                )

        accountData.delete()
    return redirect('pendingAccountList')

def rejectPendingAccount(request,id):
    accountData = PendingAccountModel.objects.get(id=id)
    accountData.status = 'Rejected'
    accountData.save()
    return redirect(pendingAccountList)


def changePassword(request):
    current_user = request.user
    if request.method == 'POST':
        oldPassword = request.POST.get('oldPassword')
        newPassword = request.POST.get('newPassword')
        confirmPassword = request.POST.get('confirmPassword')

        if check_password(oldPassword,current_user.password):
            if newPassword==confirmPassword:
                current_user.set_password(newPassword)
                current_user.save()
                update_session_auth_hash(request, current_user)
                return redirect('home')
    return render(request, 'changePasswordPage.html')