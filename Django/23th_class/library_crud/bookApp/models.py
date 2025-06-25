from django.db import models

# Create your models here.
class bookModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    published_date = models.DateField(null=True)