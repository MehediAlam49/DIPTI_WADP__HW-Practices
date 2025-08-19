from django.urls import path
from libraryApp.views import *
urlpatterns = [
    path('', book_create, name='book_create'),
    path('book_list/', book_list, name='book_list'),
    path('book_detail/<str:pk>/', book_detail, name='book_detail'),
    path('book_update/<str:pk>/', book_update, name='book_update'),
    path('book_delete/<str:pk>/', book_delete, name='book_delete'),
]