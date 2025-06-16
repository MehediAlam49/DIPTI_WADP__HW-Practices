
from django.contrib import admin
from django.urls import path
from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bookList, name='bookList'),
    path('add-Book/', addBook, name='addBook'),
    path('edit-Book/', editBook, name='editBook'),
]
