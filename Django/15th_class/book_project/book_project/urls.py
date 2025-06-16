
from django.contrib import admin
from django.urls import path
from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bookList, name='bookList'),
    path('add-Book/', addBook, name='addBook'),
    path('edit-Book/<str:id>', editBook, name='editBook'),
    path('delete-Book/<str:id>', deleteBook, name='deleteBook'),
    path('view-Book/<str:id>', viewBook, name='viewBook'),
]
