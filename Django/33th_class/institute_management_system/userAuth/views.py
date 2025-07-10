from django.shortcuts import render,redirect

# Create your views here.
def registerPage(request):
    return render(request, 'registerPage.html')
def loginPage(request):
    return render(request, 'loginPage.html')
def logoutPage(request):
    return render(request, 'logoutPage.html')