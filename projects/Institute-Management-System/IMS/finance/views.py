from django.shortcuts import render
from .models import Fee
from users.models import StudentProfile

def view_fees(request):
    student = StudentProfile.objects.get(user=request.user)
    fees = Fee.objects.filter(student=student)
    return render(request, 'finance/view_fees.html', {'fees': fees})