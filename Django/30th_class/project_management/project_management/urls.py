
from django.contrib import admin
from django.urls import path
from projectApp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registerPage, name='registerPage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),

    path('home/', home, name='home'),
    path('projectList/', projectList, name='projectList'),
    path('addProject/', addProject, name='addProject'),

    path('editProject/', editProject, name='editProject'),
    path('viewProject/', viewProject, name='viewProject'),
    path('deleteProject/', deleteProject, name='deleteProject'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
