from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=100,null=True)
    content = models.TextField(null=True)
    published_by = models.ForeignKey('users.User', on_delete=models.CASCADE,null=True)
    date_posted = models.DateField(auto_now_add=True,null=True)
