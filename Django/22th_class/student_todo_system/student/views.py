from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
# <-----------------Authenticate----------------------->
def registerPage(request):
    return render(request, 'registerPage.html')
def loginPage(request):
    return render(request, 'loginPage.html')
def logoutPage(request):
    return redirect('loginPage')


# <-----------------Home----------------------->
def home(request):
    return render(request, 'home.html')


# <-----------------student CRUD----------------------->
def addStudent(request):
    return render(request, 'addStudent.html')
def editStudent(request):
    return render(request, 'editStudent.html')
def viewStudent(request):
    return render(request, 'viewStudent.html')
def deleteStudent(request):
    return render(request, 'deleteStudent.html')


# <-----------------Task CRUD----------------------->
def addTask(request):
    return render(request, 'addTask.html')
def editTask(request):
    return render(request, 'editTask.html')
def viewTask(request):
    return render(request, 'viewTask.html')
def deleteTask(request):
    return render(request, 'deleteTask.html')