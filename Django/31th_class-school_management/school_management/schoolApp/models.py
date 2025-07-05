from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    USER_TYPE = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
    ]

    user_type = models.CharField(choices=USER_TYPE, max_length=100, null=True)

class TeacherModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=18, null=True)
    hire_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class StudentModel(models.Model):
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True)
    age = models.PositiveIntegerField(null=True)
    grade = models.CharField(max_length=20,null=True)
    enrollment_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"