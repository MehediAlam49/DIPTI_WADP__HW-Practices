from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from schoolApp.models import *

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            userData = CustomUserModel.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                user_type = user_type,
                password=confirm_password,
            )
            userData.save()
            if userData:
                TeacherModel.objects.create(
                    user = userData,
                    subject=subject,
                    phone=phone,
                    hire_date=hire_date,
                )
                return redirect('loginPage')
    return render(request, 'signupPage.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or password is incorrect')
    return render(request, 'loginPage.html')
def logoutPage(request):
    return redirect('loginPage')


def home(request):
    return render(request, 'home.html')
def studentList(request):
    return render(request, 'studentList.html')


def addStudent(request):
    return render(request, 'addStudent.html')
def editStudent(request):
    return render(request, 'editStudent.html')
def deleteStudent(request):
    return redirect('studentList')
def viewStudent(request):
    return render(request, 'viewStudent.html')