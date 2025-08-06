from django.contrib import admin
from users.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(FacultyProfile)