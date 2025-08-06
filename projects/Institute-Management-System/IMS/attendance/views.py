from django.shortcuts import render
from .models import Attendance
from users.models import StudentProfile

def mark_attendance(request):
    # TODO: Add attendance marking logic
    return render(request, 'attendance/mark_attendance.html')

def view_attendance(request):
    student = StudentProfile.objects.get(user=request.user)
    records = Attendance.objects.filter(student=student)
    return render(request, 'attendance/view_attendance.html', {'records': records})