from django.shortcuts import render, redirect
from userAuth.models import *
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_type = 'Admin'  # ✅ Hardcoded user type

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif CustomUserModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=confirm_password,
                user_type=user_type
            )
            messages.success(request, "Registration successful. Please log in.")
            return redirect('loginPage')

    return render(request, 'master/signupPage.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'master/loginPage.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'profile.html')
def teachers(request):
    return render(request, 'teachers.html')
def addTeacher(request):
    if request.method == 'POST':
        teacher_profile = request.FILES.get('teacher_profile')
        teacher_name = request.POST.get('teacher_name')
        teacher_phone = request.POST.get('teacher_phone')

        TeacherModel.objects.create(
            teacher_profile=teacher_profile,
            teacher_name=teacher_name,
            teacher_phone=teacher_phone,
        )
        return redirect('teachers')
    return render(request, 'addTeacher.html')