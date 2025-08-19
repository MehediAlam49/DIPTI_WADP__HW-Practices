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