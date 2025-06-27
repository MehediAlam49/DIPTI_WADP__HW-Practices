from django.shortcuts import render,redirect, HttpResponse
from auth_crud_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        date_of_birth = request.POST.get('date_of_birth')
        user_types = request.POST.get('user_types')

        if password == confirm_password:
            user = customUserModel.objects.create_user(
                profile_image = profile_image,
                username=username,
                full_name=full_name,
                email=email,
                password=confirm_password,
                date_of_birth=date_of_birth,
                user_types=user_types,
            )
            return redirect('loginPage')
        else:
            return redirect('passwordNotMatched')
    return render(request, 'registerPage.html')
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
    logout(request)
    return redirect('loginPage')



def home(request):
    productData = productModel.objects.all()
    return render(request, 'home.html', {'products': productData})
def addProduct(request):
    if request.method == 'POST':
        product_image = request.FILES.get('product_image')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_description = request.POST.get('product_description')

        product = productModel.objects.create(
            product_image = product_image,
            product_name = product_name,
            product_price = product_price,
            product_description = product_description,
        )
        return redirect('home')
    return render(request, 'addProduct.html')

def viewProduct(request,id):
    return render(request, 'viewProduct.html')


def editProduct(request,id):
    return render(request, 'editProduct.html')
def deleteProduct(request,id):
    return redirect('home')




def passwordNotMatched(request):
    return render(request, 'passwordNotMatched.html')
def passwordWrong(request):
    return render(request, 'passwordWrong.html')

# if request.user.user_types != 'customer':