from django.shortcuts import render,redirect
from to_do_app.models import *
from django.contrib.auth import authenticate,login,logout,hashers,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city_name = request.POST.get('city_name')
        bio = request.POST.get('bio')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            customUserModel.objects.create_user(
                image=image,
                username=username,
                full_name=full_name,
                phone=phone,
                email=email,
                address=address,
                city_name=city_name,
                bio=bio,
                password=confirm_password,
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
        else:
            return redirect('passwordWrong')
    return render(request, 'loginPage.html')
def logoutPage(request):
    return redirect('loginPage')



def home(request):
    return render(request, 'home.html')
def itemList(request):
    return render(request, 'itemList.html')



def addItem(request):
    return render(request, 'addItem.html')
def editItem(request):
    return render(request, 'editItem.html')
def viewItem(request):
    return render(request, 'viewItem.html')
def deleteItem(request):
    return render(request, 'deleteItem.html')



def passwordNotMatched(request):
    return render(request, 'passwordNotMatched.html')
def passwordWrong(request):
    return render(request, 'passwordWrong.html')