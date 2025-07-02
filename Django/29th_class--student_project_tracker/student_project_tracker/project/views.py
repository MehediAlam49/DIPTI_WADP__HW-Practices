from django.shortcuts import render,redirect,HttpResponse
from project.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            userData = customUserModel.objects.create_user(
                username=username,
                email=email,
                password=confirm_password,
            )
            if userData:
                studentModel.objects.create(
                    user = userData,
                    student_name=student_name,
                    student_id=student_id,
                )
                userData.save()
                return redirect('loginPage')
    
    return render(request, 'signupPage.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'loginPage.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')




def home(request):
    user = request.user
    if user.is_superuser:
        projectData = projectModel.objects.all()
    else:
        projectData = projectModel.objects.filter(created_by = request.user)

    return render(request, 'home.html', {'project': projectData})
def projectList(request):
    projectData = projectModel.objects.filter(created_by = request.user)
    return render(request, 'projectList.html', {'projects': projectData})


def addProject(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_description = request.POST.get('project_description')
        project_status = request.POST.get('project_status')
        deadline = request.POST.get('deadline')

        projectModel.objects.create(
            created_by = request.user,
            project_name=project_name,
            project_description=project_description,
            project_status=project_status,
            deadline=deadline,
        )
        return redirect('projectList')
    return render(request, 'addProject.html')
def editProject(request,id):
    projectData = projectModel.objects.get(id=id)
    if request.method == 'POST':
        projectData.project_name = request.POST.get('project_name')
        projectData.project_description = request.POST.get('project_description')
        projectData.project_status = request.POST.get('project_status')
        projectData.deadline = request.POST.get('deadline')

        projectData.save()
        return redirect('projectList')
    return render(request, 'editProject.html', {'project': projectData})
def viewProject(request,id):
    projectData = projectModel.objects.get(id=id)
    return render(request, 'viewProject.html', {'project': projectData})
def deleteProject(request,id):
    projectModel.objects.get(id=id).delete()
    return redirect('projectList')
def changeStatus(request,id):
    projectData = projectModel.objects.get(id=id)
    if projectData.project_status == 'NotStarted':
        projectData.project_status = 'InProgress'
    elif projectData.project_status == 'InProgress':
        projectData.project_status = 'Completed'
    projectData.save()
    return redirect('projectList')