from django.shortcuts import render,redirect

# Create your views here.
def registerPage(request):
    return render(request, 'registerPage.html')
def loginPage(request):
    return render(request, 'loginPage.html')
def logoutPage(request):
    return render(request, 'logoutPage.html')


def home(request):
    return render(request, 'home.html')
def addBook(request):
    return render(request, 'addBook.html')
def editBook(request):
    return render(request, 'editBook.html')
def viewBook(request):
    return render(request, 'viewBook.html')
def deleteBook(request):
    return redirect('home')


def passwordWrong(request):
    return render(request, 'passwordWrong.html')
def passwordNotMatched(request):
    return render(request, 'passwordNotMatched.html')