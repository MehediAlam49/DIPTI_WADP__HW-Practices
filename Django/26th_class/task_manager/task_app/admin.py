from django.contrib import admin
from task_app.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email']

admin.site.register(CustomUserModel, CustomUserAdmin)

admin.site.register(taskModel)