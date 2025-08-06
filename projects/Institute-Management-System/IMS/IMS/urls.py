from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('academics/', include('academics.urls')),
    path('attendance/', include('attendance.urls')),
    path('finance/', include('finance.urls')),
    path('infrastructure/', include('infrastructure.urls')),
    path('notices/', include('notices.urls')),
    path('support/', include('support.urls')),
]