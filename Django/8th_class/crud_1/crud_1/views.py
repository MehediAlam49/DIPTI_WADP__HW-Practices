from django.shortcuts import render
from library.models import *

def home(request):
    return render(request, 'home.html')
def book(request):
    context = {'bookData': bookModel.objects.all()}
    return render(request, 'book.html',context)
def studentList(request):
    context = {'studentData': studentModel.objects.all()}
    return render(request, 'studentList.html',context)
def addBook(request):
    return render(request, 'addBook.html')
def addStudent(request):
    return render(request, 'addStudent.html')