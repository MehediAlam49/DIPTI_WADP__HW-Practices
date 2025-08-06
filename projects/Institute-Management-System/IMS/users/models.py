from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('faculty', 'Faculty'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,null=True)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    roll_number = models.CharField(max_length=20,null=True)
    enrolled_courses = models.ManyToManyField('academics.Course')

class FacultyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    department = models.ForeignKey('infrastructure.Department', on_delete=models.SET_NULL, null=True)
