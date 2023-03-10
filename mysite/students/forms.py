from django import forms
from .models import Student

class NewStudentForm(forms.ModelForm):
    class meta:
        model = Student
        fields = ['first_name', 'last_name', 'registeration_number']
