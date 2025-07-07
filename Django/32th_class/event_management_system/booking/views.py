from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash,hashers
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
def myBooks(request):
    return render(request, 'myBooks.html')
def profile(request):
    return render(request, 'profile.html')


def addBook(request):
    return render(request, 'addBook.html')
def editBook(request):
    return render(request, 'editBook.html')
def viewBook(request):
    return render(request, 'viewBook.html')
def deleteBook(request):
    return redirect('myBooks')


def changePassword(request):
    return render(request, 'changePassword.html')
def changeStatus(request):
    return render(request, 'changeStatus.html')