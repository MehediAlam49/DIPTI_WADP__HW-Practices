from django.db import models
from user_auth_app.models import *

# Create your models here.
class CandidateProfileModel(models.Model):
    candidate_user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100,null=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.candidate_user.username