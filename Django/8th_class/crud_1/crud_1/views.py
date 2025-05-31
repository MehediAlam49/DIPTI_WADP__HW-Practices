from django.shortcuts import render
from library.models import *

def home(request):
    return render(request, 'home.html')
def book(request):
    return render(request, 'book.html')
def studentList(request):
    return render(request, 'studentList.html')
def addBook(request):
    return render(request, 'addBook.html')
def addStudent(request):
    return render(request, 'addStudent.html')