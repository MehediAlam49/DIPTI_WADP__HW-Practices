from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User

@login_required
def dashboard(request):
    role = request.user.role
    if role == 'admin':
        return redirect('admin_dashboard')
    elif role == 'faculty':
        return redirect('faculty_dashboard')
    elif role == 'student':
        return redirect('student_dashboard')
    return render(request, 'users/dashboard.html')