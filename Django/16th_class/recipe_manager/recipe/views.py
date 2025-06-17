from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def addRecipe(request):
    return render(request, 'addRecipe.html')

def editRecipe(request):
    return render(request, 'editRecipe.html')

def deleteRecipe(request):
    return redirect('home')

def viewRecipe(request):
    return render(request, 'viewRecipe.html')