#Wanjala Stephen David
# IN16/00055/20

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


class StudentMarks(forms.Form):
    cat_1 = forms.IntegerField(label="Cat 1", max_value=10)
    cat_2 = forms.IntegerField(label="Cat 2", max_value=10)
    cat_3 = forms.IntegerField(label="Cat 3", max_value=10)
    final_exam = forms.IntegerField(label="Final Exam", max_value=70)
