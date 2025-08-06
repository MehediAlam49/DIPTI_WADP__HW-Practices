from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100,null=True)

class Course(models.Model):
    title = models.CharField(max_length=100,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)

class Subject(models.Model):
    name = models.CharField(max_length=100,null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    faculty = models.ForeignKey('users.FacultyProfile', on_delete=models.SET_NULL, null=True)

class Result(models.Model):
    student = models.ForeignKey('users.StudentProfile', on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True)
    marks = models.FloatField(null=True)
    grade = models.CharField(max_length=2,null=True)
