from django.shortcuts import render
from store.models import *

def home(request):
    return render(request, 'home.html')
def user(request):
    context = {'userData': userModel.objects.all()}
    return render(request, 'user.html',context)
def books(request):
    return render(request, 'books.html')
def addStudent(request):
    return render(request, 'addStudent.html')
def addBook(request):
    return render(request, 'addBook.html')
def studentList(request):
    return render(request, 'studentList.html')
