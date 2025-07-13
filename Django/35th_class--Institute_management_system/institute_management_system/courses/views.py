from django.shortcuts import render,redirect
from courses.models import *

# Create your views here.

def addCourse(request):
    return render(request, 'course/addCourse.html')