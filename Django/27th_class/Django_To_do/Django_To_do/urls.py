
from django.contrib import admin
from django.urls import path
from to_do_app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signupPage, name='signupPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('home/', home, name='home'),
    path('itemList/', itemList, name='itemList'),

    path('addItem/', addItem, name='addItem'),
    path('editItem/', editItem, name='editItem'),
    path('viewItem/', viewItem, name='viewItem'),
    path('deleteItem/', deleteItem, name='deleteItem'),

    path('passwordNotMatched/', passwordNotMatched, name='deleteItem'),
    path('passwordWrong/', passwordWrong, name='passwordWrong'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
