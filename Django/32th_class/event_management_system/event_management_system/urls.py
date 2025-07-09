
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
    path('myBooking/', myBooking, name='myBooking'),
    path('profile/', profile, name='profile'),

    path('addBooking/', addBooking, name='addBooking'),
    path('editBooking/', editBooking, name='editBooking'),
    path('viewBooking/', viewBooking, name='viewBooking'),
    path('deleteBooking/', deleteBooking, name='deleteBooking'),

    path('changePassword/', changePassword, name='changePassword'),
    path('changeStatus/', changeStatus, name='changeStatus'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
