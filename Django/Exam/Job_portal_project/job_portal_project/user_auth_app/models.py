from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    user_type = models.CharField(choices=[('Admin','Admin'),('Employer','Employer'),('Candidate','Candidate')],null=True)
    phone = models.CharField(max_length=100, null=True)


class PendingAccountModel(models.Model):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    user_type = models.CharField(choices=[('Employer','Employer'),('Candidate','Candidate')],null=True)
    status = models.CharField(choices=[('Pending','Pending'),('Accept','Accept'),('Rejected','Rejected')],null=True)