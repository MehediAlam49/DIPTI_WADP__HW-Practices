from django.shortcuts import render, get_object_or_404
from .models import Course, Subject

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'academics/course_list.html', {'courses': courses})

def subject_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    subjects = Subject.objects.filter(course=course)
    return render(request, 'academics/subject_list.html', {'course': course, 'subjects': subjects})