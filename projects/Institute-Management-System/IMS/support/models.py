from django.db import models

class SupportTicket(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    status = models.CharField(max_length=15, choices=[('open', 'Open'), ('resolved', 'Resolved')],null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
