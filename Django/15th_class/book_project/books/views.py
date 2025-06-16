from django.shortcuts import render
from books.models import *
# Create your views here.
def bookList(request):
    bookData = bookModel.objects.all()
    return render(request, 'bookList.html', {"books": bookData})
def addBook(request):
    return render(request, 'addBook.html')
def editBook(request):
    return render(request, 'editBook.html')
def deleteBook(request):
    return render(request, 'deleteBook.html')