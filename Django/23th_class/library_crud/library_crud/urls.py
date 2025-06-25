
from django.contrib import admin
from django.urls import path
from bookApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('home/', home, name='home'),
    path('addBook/', addBook, name='addBook'),
    path('editBook/<str:id>', editBook, name='editBook'),
    path('viewBook/<str:id>', viewBook, name='viewBook'),
    path('deleteBook/<str:id>', deleteBook, name='deleteBook'),

    path('passwordWrong/', passwordWrong, name='passwordWrong'),
    path('passwordNotMatched/', passwordNotMatched, name='passwordNotMatched'),
]
