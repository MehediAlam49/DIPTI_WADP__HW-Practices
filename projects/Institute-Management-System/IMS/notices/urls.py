from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_board, name='notice_board'),
]