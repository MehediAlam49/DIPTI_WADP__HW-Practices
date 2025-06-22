from django.shortcuts import render,redirect

# Create your views here.
# <--------Home page Function-------------->
def home(request):
    return render(request, 'home.html')

# <----------addStudent page Function-------------->
def addStudent(request):
    return render(request, 'addStudent.html')

# <----------editStudent page Function-------------->
def editStudent(request):
    return render(request, 'editStudent.html')

# <----------viewStudent page Function-------------->
def viewStudent(request):
    return render(request, 'viewStudent.html')

# <----------deleteStudent page Function-------------->
def deleteStudent(request):
    return redirect('home')




# <----------loginPage Function-------------->
def loginPage(request):
    return render(request, 'loginPage.html')

# <----------logoutPage Function-------------->
def logoutPage(request):
    return render(request, 'logoutPage.html')

# <----------signupPage Function-------------->
def signupPage(request):
    return render(request, 'signupPage.html')

# <----------passwordNotMatched Function-------------->
def passwordNotMatched(request):
    return render(request, 'passwordNotMatched.html')

# <----------passwordWrong Function-------------->
def passwordWrong(request):
    return render(request, 'passwordWrong.html')