from django import forms
from .models import Student

class Input(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'registeration_number')

