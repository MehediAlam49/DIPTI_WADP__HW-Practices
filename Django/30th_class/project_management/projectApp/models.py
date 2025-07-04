from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class customUserModel(AbstractUser):
    USER_TYPE = [
        ('Recruiter','Recruiter'),
        ('Seeker','Seeker'),
    ]
    user_profile = models.ImageField(upload_to='media/users',null=True, blank=True)
    full_name = models.CharField(max_length=100,null=True, blank=True)
    phone = models.CharField(max_length=17,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    user_type = models.CharField(choices=USER_TYPE,max_length=100,null=True, blank=True)

class jobModel(models.Model):
    JOB_STATUS = [
        ('Full_time','Full_time'),
        ('Part_time','Part_time'),
    ]
    company_logo = models.ImageField(upload_to='media/company_logo',null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True,blank=True)
    job_description = models.TextField(null=True,blank=True)
    experience = models.IntegerField(null=True,blank=True)
    job_status = models.CharField(choices=JOB_STATUS,max_length=100,null=True,blank=True)
    created_by = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateField(auto_now=True,null=True,blank=True)