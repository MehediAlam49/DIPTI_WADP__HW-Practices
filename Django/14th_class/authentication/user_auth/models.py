from django.db import models

# Create your models here.
class userAuthModel(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=14)
    password = models.CharField(max_length=20)