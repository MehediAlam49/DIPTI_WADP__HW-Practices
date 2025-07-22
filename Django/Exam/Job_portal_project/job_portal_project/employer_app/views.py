from django.shortcuts import render,redirect
from employer_app.models import *

# Create your views here.
def applyJob(request):
    return render(request, 'applyJob.html')
def jobList(request):
    return render(request, 'jobList.html')