from django.db import models
from user_auth_app.models import *

# Create your models here.
class EmployerProfileModel(models.Model):
    employer_user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    about_company = models.TextField(null=True)
    company_logo = models.ImageField(upload_to='media/company-logo',null=True)
    location = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.employer_user.username

class JobModel(models.Model):
    employer = models.ForeignKey(EmployerProfileModel, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    requirements = models.CharField(max_length=200, null=True)
    salary = models.CharField(max_length=100,null=True)
    job_type = models.CharField(choices=[('Full_time','Full_time'),('Remote','Remote'),('Internship','Internship')])
    deadline = models.DateField(null=True)
    posted_date = models.DateTimeField(auto_now_add=True,null=True)
    