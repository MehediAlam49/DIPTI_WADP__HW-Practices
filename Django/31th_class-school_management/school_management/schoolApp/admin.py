from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from schoolApp.models import *

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(StudentModel)
admin.site.register(TeacherModel)