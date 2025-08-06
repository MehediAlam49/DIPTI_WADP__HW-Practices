from django.db import models

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True,null=True)
    code = models.CharField(max_length=20, unique=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    title = models.CharField(max_length=100,null=True)
    level = models.PositiveIntegerField(help_text="Rank level for hierarchy sorting",null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    is_teaching_role = models.BooleanField(default=False,null=True)

    def __str__(self):
        return f"{self.title} ({self.department.code})"

# Optional: Location or facility info
class Building(models.Model):
    name = models.CharField(max_length=100,null=True)
    code = models.CharField(max_length=10, unique=True,null=True)
    address = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
