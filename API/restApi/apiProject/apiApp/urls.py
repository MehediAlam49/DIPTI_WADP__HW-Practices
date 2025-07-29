from django.urls import path
from apiApp.views import *

urlpatterns = [
    path('add-student/', addStudent, name='addStudent'),
    path('student-list/', studentList, name='studentList'),
    path('edit-student/<str:pk>/', editStudent, name='editStudent'),
    path('delete-student/<str:pk>/', deleteStudent, name='deleteStudent'),
]