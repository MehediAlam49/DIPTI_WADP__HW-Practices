from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    profile_picture = models.ImageField(upload_to='media/profile', null=True)
    bio = models.TextField(null=True)

class taskModel(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    due_date = models.DateField(null=True)
    priority = models.CharField(max_length=100, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], null=True)
    status = models.CharField(max_length=100, choices=[('pending', 'Pending'), ('inProgress', 'InProgress'), ('completed', 'Completed')], null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)