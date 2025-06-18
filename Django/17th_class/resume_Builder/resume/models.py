from django.db import models

# Create your models here.
class resumeModel(models.Model):
    fullName = models.CharField(max_length=100, null=True)
    profilePic = models.ImageField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=18, null=True)
    address = models.TextField(null=True)
    summary = models.TextField(null=True)
    degree = models.CharField(max_length=100, null=True)
    institute = models.CharField(max_length=100, null=True)
    graduationYear = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=255, null=True)
    skills = models.CharField(max_length=255, null=True)
    hobbies = models.CharField(max_length=255, null=True)
    achievements = models.TextField(null=True)