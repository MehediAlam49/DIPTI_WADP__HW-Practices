from django.shortcuts import render,redirect
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
    pass