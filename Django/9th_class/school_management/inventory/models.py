from django.db import models

# Create your models here.
class courseModel(models.Model):
    name =models.CharField(max_length=100)
    credits = models.IntegerField()
    instructor = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

class studentModel(models.Model):
    name =models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

class teacherModel(models.Model):
    name =models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)