from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUserModel(AbstractUser):
    USER_TYPE = [
        ('Teacher', 'Teacher'),
        ('student', 'student'),
    ]

    user_types = models.CharField(choices=USER_TYPE, max_length=100, null=True, blank=True)


class teacherModel(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)