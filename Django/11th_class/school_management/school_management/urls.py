
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
    path('editStudent/<str:myid>', editStudent, name='editStudent'),
    path('deleteStudent/<str:myid>', deleteStudent, name='deleteStudent'),
    path('viewStudent/<str:myid>', viewStudent, name='viewStudent'),
    path('studentList/', studentList, name='studentList'),

    path('addTeacher/', addTeacher, name='addTeacher'),
    path('editTeacher/<str:myid>', editTeacher, name='editTeacher'),
    path('deleteTeacher/<str:myid>', deleteTeacher, name='deleteTeacher'),
    path('viewTeacher/<str:myid>', viewTeacher, name='viewTeacher'),
    path('teacherList/', teacherList, name='teacherList'),
]
