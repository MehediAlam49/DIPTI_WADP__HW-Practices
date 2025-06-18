
from django.contrib import admin
from django.urls import path
from resume.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add-Resume/', addResume, name='addResume'),
    path('edit-Resume/<str:id>', editResume, name='editResume'),
    path('view-Resume/<str:id>', viewResume, name='viewResume'),
    path('delete-Resume/<str:id>', deleteResume, name='deleteResume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
