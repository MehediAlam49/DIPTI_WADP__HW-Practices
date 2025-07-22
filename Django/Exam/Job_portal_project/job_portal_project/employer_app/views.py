from django.shortcuts import render,redirect
from employer_app.models import *
from employer_app.forms import *

# Create your views here.
def addJob(request):
    if request.method == 'POST':
        job_form = JobModelForm(request.POST)
        employer_data = EmployerProfileModel.objects.get(employer_user = request.user)
        if job_form.is_valid():
            job_form_data = job_form.save(commit=False)
            job_form_data.employer = employer_data
            job_form_data.save()
            return redirect('jobList')
    else:
        job_form = JobModelForm()
    return render(request, 'addJob.html',{'job_form':job_form})

def jobList(request):
    employer_data = EmployerProfileModel.objects.get(employer_user = request.user)
    jobData = JobModel.objects.filter(employer = employer_data)
    return render(request, 'jobList.html',{'jobData': jobData})


def editJob(request, id):
    jobData = JobModel.objects.get(id=id)
    if request.method == 'POST':
        formData = JobModelForm(request.POST,instance=jobData)
        if formData.is_valid():
            formData.save()
            return redirect('jobList')
    else:
        formData = JobModelForm(instance=jobData)
    return render(request, 'editJob.html', {'formData':formData})
def viewJob(request, id):
    jobData = JobModel.objects.get(id=id)
    return render(request, 'viewJob.html',{'jobData':jobData})
def deleteJob(request, id):
    JobModel.objects.get(id=id).delete()
    return redirect('jobList')