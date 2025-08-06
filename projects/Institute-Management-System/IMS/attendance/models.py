from django.db import models

class Attendance(models.Model):
    student = models.ForeignKey('users.StudentProfile', on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey('academics.Subject', on_delete=models.CASCADE,null=True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')],null=True)
