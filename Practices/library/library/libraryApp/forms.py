from django import forms
from libraryApp.models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'