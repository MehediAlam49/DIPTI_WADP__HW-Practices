

from django import forms
from libraryApp.models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'

 #Student form       
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'