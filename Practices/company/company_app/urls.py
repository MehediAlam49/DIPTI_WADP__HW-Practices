from django.urls import path
from company_app.views import *

urlpatterns = [
    path('', company_list, name='company_list'),
    path('create_company/', create_company, name='create_company'),
    path('edit_company/<str:id>', edit_company, name='edit_company'),
    path('delete_company/<str:id>', delete_company, name='delete_company'),


    path('employee_list/', employee_list, name='employee_list'),
    path('create_employee/', create_employee, name='create_employee'),
    path('edit_employee/<str:id>', edit_employee, name='edit_employee'),
    path('delete_employee/<str:id>', delete_employee, name='delete_employee'),
]