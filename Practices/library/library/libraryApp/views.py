from django.shortcuts import render,redirect,get_object_or_404
from libraryApp.models import *
from libraryApp.forms import *

# Create your views here.
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_create.html',{'form':form})

def book_list(request):
    books = BookModel.objects.all()
    return render(request, 'book_list.html',{'books':books})

def book_detail(request,pk):
    book = get_object_or_404(BookModel,pk=pk)
    return render(request, 'book_detail.html',{'book':book})

def book_update(request,pk):
    book = get_object_or_404(BookModel,pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_update.html',{'form':form})

def book_delete(request,pk):
    get_object_or_404(BookModel,pk=pk).delete()
    return redirect('book_list')

#Student section
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = StudentForm()
    return render(request, 'student_create.html',{'form':form})

def student_list(request):
    books = StudentModel.objects.all()
    return render(request, 'student_list.html',{'students':students})

def student_detail(request,pk):
    student = get_object_or_404(StudentModel,pk=pk)
    return render(request, 'student_detail.html',{'student':student})

def student_update(request,pk):
    student = get_object_or_404(BookModel,pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_update.html',{'form':form})

def student_delete(request,pk):
    get_object_or_404(StudentModel,pk=pk).delete()
    return redirect('student_list')