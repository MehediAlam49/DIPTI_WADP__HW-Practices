from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    company_name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.company_name
    

class EmployeeModel(models.Model):
    employee_name = models.CharField(max_length=100, null=True)
    email = models.EmailField( null=True)
    department = models.CharField(choices=[('HR','HR'),('Manager','Manager'),('Staff','Staff'),],max_length=20, null=True)
    def __str__(self):
        return self.employee_name