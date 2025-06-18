from django.shortcuts import render, redirect
from store.models import *

def home(request):
    return render(request, 'home.html')
def user(request):
    context = {'userData': userModel.objects.all()}
    return render(request, 'user.html',context)
def books(request):
    context = {'booksData': booksModel.objects.all()}
    return render(request, 'books.html',context)
def studentList(request):
    context = {'studentData': studentModel.objects.all()}
    return render(request, 'studentList.html',context)
def addStudent(request):
    if request.method == 'POST':
        student = studentModel(
        name = request.POST.get('name'),
        department = request.POST.get('department'),
        semester = request.POST.get('semester'),
        age = request.POST.get('age'),
        phone = request.POST.get('phone')
        )
        student.save()
        return redirect("studentList")
    return render(request, 'addStudent.html')
def addBook(request):
    if request.method == 'POST':
        book = booksModel(
        title = request.POST.get('title'),
        author = request.POST.get('author'),
        price = request.POST.get('price'),
        stock = request.POST.get('stock'),
        publish_date = request.POST.get('publish_date'),
        )
        book.save()
        return redirect("books")
    return render(request, 'addBook.html')
