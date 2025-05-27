
from django.contrib import admin
from django.urls import path

from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
