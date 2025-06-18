from django.shortcuts import render
from myApp.models import *

# Create your views here.
def viewStudent(request):
    person = Person.objects.all()
    context = {'data': person}

    return render(request, 'viewStudent.html', context)