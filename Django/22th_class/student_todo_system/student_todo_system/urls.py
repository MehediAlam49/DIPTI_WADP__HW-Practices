
from django.contrib import admin
from django.urls import path
from student.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # <-----------------Authenticate----------------------->
    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    # <-----------------Home----------------------->
    path('home/', home, name='home'),

    # <-----------------student CRUD----------------------->
    path('addStudent/', addStudent, name='addStudent'),
    path('viewStudent/', viewStudent, name='viewStudent'),
    path('editStudent/', editStudent, name='editStudent'),
    path('deleteStudent/', deleteStudent, name='deleteStudent'),
    path('studentList/', studentList, name='studentList'),


    # <-----------------Task CRUD----------------------->
    path('addTask/', addTask, name='addTask'),
    path('viewTask/', viewTask, name='viewTask'),
    path('editTask/', editTask, name='editTask'),
    path('deleteTask/', deleteTask, name='deleteTask'),
    path('taskList/', taskList, name='taskList'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
