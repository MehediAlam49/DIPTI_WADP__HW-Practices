from django.urls import path
from libraryApp.views import *
urlpatterns = [
    path('', book_create, name='book_create')
]