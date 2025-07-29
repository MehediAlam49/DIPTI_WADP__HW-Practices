from django.urls import path
from apiApp.views import *

urlpatterns = [
    path('add-student/', addStudent, name='addStudent'),
    path('student-list/', studentList, name='studentList'),
]