from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),     # You can implement this
    path('logout/', views.logout_view, name='logout'),   # Optional
]