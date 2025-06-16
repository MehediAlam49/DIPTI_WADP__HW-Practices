from django.shortcuts import render

# Create your views here.
def bookList(request):
    return render(request, 'bookList.html')
def addBook(request):
    return render(request, 'addBook.html')
def editBook(request):
    return render(request, 'editBook.html')
def deleteBook(request):
    return render(request, 'deleteBook.html')