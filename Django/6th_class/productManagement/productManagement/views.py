from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def product(request):
    return render(request, 'product.html')
def addProduct(request):
    return render(request, 'addProduct.html')
def addCustomer(request):
    return render(request, 'addCustomer.html')
def customer(request):
    return render(request, 'customer.html')