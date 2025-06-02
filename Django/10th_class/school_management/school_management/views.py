from django.shortcuts import render,redirect
from inventory.models import *

def home(request):
    return render(request, 'home.html')

def addCourse(request):
    if request.method == 'POST':
        course = courseModel(
            name = request.POST.get('name'),
            credits = request.POST.get('credits'),
            instructor = request.POST.get('instructor'),
            level = request.POST.get('level'),
        )
        course.save()
        return redirect('courseList')
    return render(request, 'addCourse.html')
def editCourse(request):
    return render(request, 'editCourse.html')
def courseList(request):
    query = {'courseData': courseModel.objects.all()}
    return render(request, 'courseList.html',query)

def addStudent(request):
    if request.method == 'POST':
        student = studentModel(
            name = request.POST.get('name'),
            class_name = request.POST.get('class_name'),
            gender = request.POST.get('gender'),
            address = request.POST.get('address'),
        )
        student.save()
        return redirect('studentList')
    return render(request, 'addStudent.html')
def editStudent(request):
    return render(request, 'editStudent.html')
def studentList(request):
    query ={'studentData': studentModel.objects.all()}
    return render(request, 'studentList.html',query)

def addTeacher(request):
    if request.method == 'POST':
        teacher = teacherModel(
            name = request.POST.get('name'),
            designation = request.POST.get('designation'),
            gender = request.POST.get('gender'),
            address = request.POST.get('address'),
        )
        teacher.save()
        return redirect('teacherList')
    return render(request, 'addTeacher.html')
def editTeacher(request):
    return render(request, 'editTeacher.html')
def teacherList(request):
    query = {'teacherData': teacherModel.objects.all()}
    return render(request, 'teacherList.html',query)
