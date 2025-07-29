from django.db import models

# Create your models here.
class StudentModel(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    student_name = models.CharField(max_length=100, null=True)
    student_roll = models.IntegerField(null=True,blank=True)
    student_age = models.PositiveBigIntegerField( null=True)
    student_address = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.student_name