from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[('Admin','Admin'),('Teacher','Teacher')])

    def __str__(self):
        return self.user_type
    
class TeacherModel(models.Model):
    teacher_name = models.CharField(max_length=100, null=True)
    last_education = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.teacher_name
    

class StudentBasicInfoModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class StudentEducationInfoModel(models.Model):
    student = models.ForeignKey(StudentBasicInfoModel,on_delete=models.CASCADE, null=True)
    degree_name = models.CharField(max_length=100, null=True)
    grade = models.CharField(max_length=100, null=True)
    passing_year = models.PositiveIntegerField(null=True)