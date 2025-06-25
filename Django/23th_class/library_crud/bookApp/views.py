from django.shortcuts import render,redirect
from bookApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    if request.method =='POST':
        userName = request.POST.get('userName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create_user(userName,email, password)
            user.save()
            return redirect(loginPage)
        else:
            return redirect('passwordNotMatched')
    return render(request, 'registerPage.html')
def loginPage(request):
    if request.method =='POST':
        userName = request.POST.get('userName')
        password = request.POST.get('password')

        user = authenticate(username = userName, password = password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('passwordWrong')
    return render(request, 'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def home(request):
    bookData = bookModel.objects.all()
    return render(request, 'home.html', {'books': bookData})
def addBook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')

        books = bookModel(
            title = title,
            author = author,
            description = description,
            published_date = published_date,
        )
        books.save()
        return redirect('home')
    return render(request, 'addBook.html')
def editBook(request,id):
    return render(request, 'editBook.html')
def viewBook(request,id):
    return render(request, 'viewBook.html')

def deleteBook(request,id):
    return redirect('home')


def passwordWrong(request):
    return render(request, 'passwordWrong.html')
def passwordNotMatched(request):
    return render(request, 'passwordNotMatched.html')