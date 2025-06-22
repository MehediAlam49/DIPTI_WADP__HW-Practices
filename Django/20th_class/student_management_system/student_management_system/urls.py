
from django.contrib import admin
from django.urls import path
from studentApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addStudent/', addStudent, name='addStudent'),
    path('editStudent/', editStudent, name='editStudent'),
    path('viewStudent/', viewStudent, name='viewStudent'),
    path('deleteStudent/', deleteStudent, name='deleteStudent'),

    
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('signupPage/', signupPage, name='signupPage'),
    path('passwordNotMatched/', passwordNotMatched, name='passwordNotMatched'),
    path('passwordWrong/', passwordWrong, name='passwordWrong'),
]
