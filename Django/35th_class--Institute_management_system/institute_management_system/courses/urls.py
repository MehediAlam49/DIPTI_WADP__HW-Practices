from django.urls import path
from courses.views import *

urlpatterns = [
    # ----------Authenticate urls---------------
    path('addCourse/', addCourse, name='addCourse'),
    path('courses/', courses, name='courses'),
    path('admitCourse/', admitCourse, name='admitCourse'),
    path('admittedCourseList/', admittedCourseList, name='admittedCourseList'),
    path('makePayment/', makePayment, name='makePayment'),
    path('paymentList/', paymentList, name='paymentList'),
]