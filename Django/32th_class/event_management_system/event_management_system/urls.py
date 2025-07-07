
from django.contrib import admin
from django.urls import path
from booking.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signupPage, name='signupPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('home/', home, name='home'),
    path('myBooks/', myBooks, name='myBooks'),
    path('profile/', profile, name='profile'),

    path('addBook/', addBook, name='addBook'),
    path('editBook/', editBook, name='editBook'),
    path('viewBook/', viewBook, name='viewBook'),
    path('deleteBook/', deleteBook, name='deleteBook'),

    path('changePassword/', changePassword, name='changePassword'),
    path('changeStatus/', changeStatus, name='changeStatus'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
