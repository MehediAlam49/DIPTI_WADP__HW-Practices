
from django.contrib import admin
from django.urls import path
from auth_crud_app.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerPage/', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('', home, name='home'),

    path('addProduct/', addProduct, name='addProduct'),
    path('editProduct/<str:id>', editProduct, name='editProduct'),
    path('viewProduct/<str:id>', viewProduct, name='viewProduct'),
    path('deleteProduct/<str:id>', deleteProduct, name='deleteProduct'),



    path('passwordNotMatched/', passwordNotMatched, name='passwordNotMatched'),
    path('passwordWrong/', passwordWrong, name='passwordNotMatched'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
