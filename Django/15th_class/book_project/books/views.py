from django.shortcuts import render, redirect
from books.models import *
# Create your views here.
def bookList(request):
    bookData = bookModel.objects.all()
    return render(request, 'bookList.html', {"books": bookData})
def addBook(request):
    if request.method == "POST":
        books = bookModel(
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            publishedDate = request.POST.get('publishedDate'),
            description = request.POST.get('description'),
        )
        books.save()
        return redirect('bookList')
    return render(request, 'addBook.html')
def editBook(request,id):
    bookData = bookModel.objects.get(id=id)
    if request.method == "POST":
        books = bookModel(
            id = id,
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            publishedDate = request.POST.get('publishedDate'),
            description = request.POST.get('description'),
        )
        books.save()
        return redirect('bookList')
    return render(request, 'editBook.html', {'books':bookData})
def deleteBook(request,id):
    books = bookModel.objects.get(id=id).delete()
    return redirect('bookList')

def viewBook(request,id):
    bookData = bookModel.objects.get(id=id)
    return render(request, 'viewBook.html', {"books": bookData})