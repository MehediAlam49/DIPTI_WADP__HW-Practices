from django.db import models

# Create your models here.

class booksModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    publish_date = models.DateField()

class userModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.IntegerField()

class studentModel(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
