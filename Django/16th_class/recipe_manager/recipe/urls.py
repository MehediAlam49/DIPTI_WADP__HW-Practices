from django.contrib import admin
from django.urls import path
from recipe.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add-Recipe/', addRecipe, name='addRecipe'),
    path('edit-Recipe/', editRecipe, name='editRecipe'),
    path('delete-Recipe/', deleteRecipe, name='deleteRecipe'),
    path('view-Recipe/', viewRecipe, name='viewRecipe'),
]
