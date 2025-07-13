from django.shortcuts import render,redirect
from courses.models import *

# Create your views here.

def addCourse(request):
    teacherData = TeacherModel.objects.all()

    if request.method == 'POST':
        course_title = request.POST.get('course_title')
        course_description = request.POST.get('course_description')
        course_duration = request.POST.get('course_duration')
        course_duration = request.POST.get('course_duration')
        course_start_date = request.POST.get('course_start_date')
        course_fee = request.POST.get('course_fee')
        assign_teacher = request.POST.get('assign_teacher')

        teacher = TeacherModel.objects.get(id = assign_teacher)

        CourseModel.objects.create(
            course_title=course_title,
            course_description=course_description,
            course_duration=course_duration,
            course_start_date=course_start_date,
            course_fee=course_fee,
            assign_teacher=teacher,
        )
        return redirect('courses')
    return render(request, 'course/addCourse.html', {'teacherData':teacherData})

def courses(request):
    courseData = CourseModel.objects.all()
    return render(request, 'course/courses.html', {'courseInfo': courseData})

def admitCourse(request):
    studentData = StudentModel.objects.all()
    courseData = CourseModel.objects.all()

    context = {
        'student':studentData,
        'course':courseData,
    }

    if request.method == 'POST':
        student = request.POST.get('student')
        admitted_course = request.POST.get('admitted_course')
        payment = request.POST.get('payment')

        studentData = StudentModel.objects.get(id=student)
        courseData = CourseModel.objects.get(id=admitted_course)
        course_fee = courseData.course_fee
        due = int(course_fee) - int(payment)

        admitted_course_data=AdmittedCourseModel.objects.create(
            student = studentData,
            admitted_course=courseData,
            payment=payment,
            course_fee=course_fee,
            due=due,

        )

        PaymentHistoryModel.objects.create(
            admitted_course=admitted_course_data,
            payment=payment,
        )
        return redirect('admittedCourseList')
        
    return render(request, 'course/admitCourse.html', context)

def admittedCourseList(request):
    admittedCourseData = AdmittedCourseModel.objects.all()
    return render(request, 'course/admittedCourseList.html',{'admittedCourseData':admittedCourseData})

def makePayment(request):
    admit_course_list = AdmittedCourseModel.objects.all()
    if request.method == 'POST':
        admitted_course = request.POST.get('admitted_course')
        payment = request.POST.get('payment')

        admittedCourseData = AdmittedCourseModel.objects.get(id=admitted_course)

        old_payment = admittedCourseData.payment
        new_payment = int(old_payment) + int(payment)
        admittedCourseData.payment=new_payment

        due = admittedCourseData.course_fee - admittedCourseData.payment
        admittedCourseData.due = due

        admittedCourseData.save()

        PaymentHistoryModel.objects.create(
            admitted_course = admittedCourseData,
            payment=payment,
        )
        return redirect('admittedCourseList')
    return render(request, 'payment/makePayment.html', {'admit_course_list':admit_course_list})

def paymentList(request):
    paymentData = PaymentHistoryModel.objects.all()
    return render(request, 'payment/paymentList.html', {'paymentData':paymentData})

