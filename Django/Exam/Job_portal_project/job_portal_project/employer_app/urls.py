from django.urls import path
from employer_app.views import *

urlpatterns = [
    path('apply-job/', applyJob, name='applyJob'),
    path('job-list/', jobList, name='jobList'),
]