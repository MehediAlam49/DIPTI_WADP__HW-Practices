
from django.contrib import admin
from django.urls import path
from userAuth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
]
