from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

# Create your views here.
def signupPage(request):
    return render(request, 'signupPage.html')
def loginPage(request):
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