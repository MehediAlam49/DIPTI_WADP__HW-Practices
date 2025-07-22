from django.urls import path
from employer_app.views import *

urlpatterns = [
    path('add-job/', addJob, name='addJob'),
    path('job-list/', jobList, name='jobList'),
    path('edit-job/<str:id>', editJob, name='editJob'),
    path('view-job/<str:id>', viewJob, name='viewJob'),
    path('delete-job/<str:id>', deleteJob, name='deleteJob'),
]