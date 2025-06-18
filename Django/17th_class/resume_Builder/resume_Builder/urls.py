
from django.contrib import admin
from django.urls import path
from resume.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add-Resume', addResume, name='addResume'),
    path('edit-Resume', editResume, name='editResume'),
    path('view-Resume', viewResume, name='viewResume'),
    path('delete-Resume', deleteResume, name='deleteResume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
