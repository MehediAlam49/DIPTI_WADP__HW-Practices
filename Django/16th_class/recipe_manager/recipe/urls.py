from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from recipe.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add-Recipe/', addRecipe, name='addRecipe'),
    path('edit-Recipe/<str:id>', editRecipe, name='editRecipe'),
    path('delete-Recipe/<str:id>', deleteRecipe, name='deleteRecipe'),
    path('view-Recipe/<str:id>', viewRecipe, name='viewRecipe'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
