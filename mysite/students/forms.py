from django import forms
from .models import Student

class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'registeration_number', 'major_course_of_study')


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'registeration_number', 'major_course_of_study')


