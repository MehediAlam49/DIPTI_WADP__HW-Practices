from django.db import models

class Fee(models.Model):
    student = models.ForeignKey('users.StudentProfile', on_delete=models.CASCADE,null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2,null=True)
    due_date = models.DateField(null=True)
    status = models.CharField(max_length=10, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')],null=True)
