from django.shortcuts import render,redirect,HttpResponse
from projectApp.models import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    return render(request, 'registerPage.html')
def loginPage(request):
    return render(request, 'loginPage.html')
def logoutPage(request):
    return redirect('loginPage')



def home(request):
    return render(request, 'home.html')
def projectList(request):
    return render(request, 'projectList.html')

def addProject(request):
    return render(request, 'addProject.html')
def viewProject(request):
    return render(request, 'viewProject.html')
def editProject(request):
    return render(request, 'editProject.html')
def deleteProject(request):
    return render(request, 'deleteProject.html')