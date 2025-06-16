from django.db import models

# Create your models here.
class bookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publishedDate = models.DateField()
    description = models.TextField(max_length=200)