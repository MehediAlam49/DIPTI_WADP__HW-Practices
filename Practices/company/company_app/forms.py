from django import forms
from company_app.models import *

class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyModel
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'