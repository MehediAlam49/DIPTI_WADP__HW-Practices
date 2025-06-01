from django.shortcuts import render,redirect
from inventory.models import *

def home(request):
    return render(request, 'home.html')

def addCourse(request):
    return render(request, 'addCourse.html')
def editCourse(request):
    return render(request, 'editCourse.html')
def courseList(request):
    return render(request, 'courseList.html')

def addStudent(request):
    return render(request, 'addStudent.html')
def editStudent(request):
    return render(request, 'editStudent.html')
def studentList(request):
    return render(request, 'studentList.html')

def addTeacher(request):
    return render(request, 'addTeacher.html')
def editTeacher(request):
    return render(request, 'editTeacher.html')
def teacherList(request):
    return render(request, 'teacherList.html')
