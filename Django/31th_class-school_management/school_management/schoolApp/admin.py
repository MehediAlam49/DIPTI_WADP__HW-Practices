from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from schoolApp.models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ['username','first_name','user_type']

admin.site.register(CustomUserModel,CustomUserAdmin)
admin.site.register(StudentModel)
admin.site.register(TeacherModel)