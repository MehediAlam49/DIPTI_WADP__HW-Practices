from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    USER_TYPE = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
    ]
    user_type = models.CharField(choices=USER_TYPE, max_length=100, null=True, blank=True)

class TeacherModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='teacher_profile')
    subject = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=18, null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class StudentModel(models.Model):
    teacher = models.ForeignKey(TeacherModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, related_name='student_profile')
    age = models.PositiveIntegerField(null=True, blank=True)
    grade = models.CharField(max_length=20, null=True, blank=True)
    enrollment_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
