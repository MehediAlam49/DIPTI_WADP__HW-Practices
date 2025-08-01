from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_create, name='product_list_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
]
