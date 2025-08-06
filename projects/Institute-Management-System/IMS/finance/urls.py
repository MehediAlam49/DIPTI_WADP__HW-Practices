from django.urls import path
from . import views

urlpatterns = [
    path('fees/', views.view_fees, name='view_fees'),
]