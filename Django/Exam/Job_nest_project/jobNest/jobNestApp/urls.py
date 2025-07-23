from django.urls import path
from jobNestApp.views import *

urlpatterns = [
    path('',registerPage, name='registerPage'),
    path('loginPage/',loginPage, name='loginPage'),
    path('logoutPage/',logoutPage, name='logoutPage'),
    path('home/',home, name='home'),
    path('profile/',profile, name='profile'),
]