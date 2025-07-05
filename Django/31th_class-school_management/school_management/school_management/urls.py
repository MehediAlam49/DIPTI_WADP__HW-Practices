
from django.contrib import admin
from django.urls import path
from schoolApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signupPage,name='signupPage'),
    path('loginPage/', loginPage,name='loginPage'),
    path('logoutPage/', logoutPage,name='logoutPage'),


    path('home/', home,name='home'),
    path('studentList/', studentList,name='studentList'),
    
    path('addStudent/', addStudent,name='addStudent'),
    path('viewStudent/', viewStudent,name='viewStudent'),
    path('editStudent/', editStudent,name='editStudent'),
    path('deleteStudent/', deleteStudent,name='deleteStudent'),
]
