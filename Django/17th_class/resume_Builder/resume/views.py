from django.shortcuts import render,redirect
from resume.models import *

# Create your views here.
def home(request):
    resumeData = resumeModel.objects.all()
    return render(request, 'home.html', {'resume':resumeData})
def addResume(request):
    if request.method == 'POST':
        resume = resumeModel(
            fullName = request.POST.get('fullName'),
            profilePic = request.FILES.get('profilePic'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            address = request.POST.get('address'),
            summary = request.POST.get('summary'),
            degree = request.POST.get('degree'),
            institute = request.POST.get('institute'),
            graduationYear = request.POST.get('graduationYear'),
            company = request.POST.get('company'),
            position = request.POST.get('position'),
            experience = request.POST.get('experience'),
            skills = request.POST.get('skills'),
            hobbies = request.POST.get('hobbies'),
            achievements = request.POST.get('achievements'),

        )
        resume.save()
        return redirect('home')
    return render(request, 'addResume.html')
def editResume(request,id):
    resumeData = resumeModel.objects.get(id=id)
    if request.method == 'POST':
        resumeData.fullName = request.POST.get('fullName')
        resumeData.email = request.POST.get('email')
        resumeData.phone = request.POST.get('phone')
        resumeData.address = request.POST.get('address')
        resumeData.summary = request.POST.get('summary')
        resumeData.degree = request.POST.get('degree')
        resumeData.institute = request.POST.get('institute')
        resumeData.graduationYear = request.POST.get('graduationYear')
        resumeData.company = request.POST.get('company')
        resumeData.position = request.POST.get('position')
        resumeData.experience = request.POST.get('experience')
        resumeData.skills = request.POST.get('skills')
        resumeData.hobbies = request.POST.get('hobbies')
        resumeData.achievements = request.POST.get('achievements')

        picture = request.FILES.get('profilePic')
        if picture is not None:
            resumeData.profilePic = picture
        resumeData.save()
        return redirect('home')
    return render(request, 'editResume.html', {'resume':resumeData})
def viewResume(request,id):
    resumeData = resumeModel.objects.get(id=id)
    return render(request, 'viewResume.html', {'resume': resumeData})
def deleteResume(request,id):
    resume = resumeModel.objects.get(id=id).delete()
    return redirect('home')