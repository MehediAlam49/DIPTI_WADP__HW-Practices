from django.shortcuts import render,redirect
from recipe.models import *

# Create your views here.
def home(request):
    recipeData = recipeModel.objects.all()
    return render(request, 'home.html',{'recipes':recipeData})

def addRecipe(request):
    if request.method == 'POST':
        recipes = recipeModel(
            recipeTitle = request.POST.get('recipeTitle'),
            recipeDescription = request.POST.get('recipeDescription'),
            recipeIngredients = request.POST.get('recipeIngredients'),
            recipeInstructions = request.POST.get('recipeInstructions'),
            recipeImage = request.FILES.get('recipeImage'),
        )
        recipes.save()
        return redirect('home')
    return render(request, 'addRecipe.html')

def editRecipe(request,id):
    recipeData = recipeModel.objects.get(id=id)
    if request.method == 'POST':
        recipeData.recipeTitle = request.POST.get('recipeTitle')
        recipeData.recipeDescription = request.POST.get('recipeDescription')
        recipeData.recipeIngredients = request.POST.get('recipeIngredients')
        recipeData.recipeInstructions = request.POST.get('recipeInstructions')

        picture = request.FILES.get('recipeImage')
        if picture is not None:
            recipeData.recipeImage = picture
        recipeData.save()
        return redirect('home')
    return render(request, 'editRecipe.html', {'recipe': recipeData})

def deleteRecipe(request,id):
    recipe = recipeModel.objects.get(id=id).delete()
    return redirect('home')

def viewRecipe(request,id):
    return render(request, 'viewRecipe.html')