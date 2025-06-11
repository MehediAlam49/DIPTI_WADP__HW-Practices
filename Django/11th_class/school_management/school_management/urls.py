
from django.contrib import admin
from django.urls import path
from school_management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
    path('addCourse/', addCourse, name='addCourse'),
    path('editCourse/<str:myid>', editCourse, name='editCourse'),
    path('deleteCourse/<str:myid>', deleteCourse, name='deleteCourse'),
    path('viewCourse/<str:myid>', viewCourse, name='viewCourse'),
    path('courseList/', courseList, name='courseList'),

    path('addStudent/', addStudent, name='addStudent'),
    path('studentList/', studentList, name='studentList'),
    path('editStudent/', editStudent, name='editStudent'),

    path('addTeacher/', addTeacher, name='addTeacher'),
    path('editTeacher/', editTeacher, name='editTeacher'),
    path('teacherList/', teacherList, name='teacherList'),
]
