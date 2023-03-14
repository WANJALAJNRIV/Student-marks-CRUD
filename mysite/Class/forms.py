from django import forms
from .models import Class, ClassEnrollment

class NewClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('class_name', 'unit_code')


class EditClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('class_name', 'unit_code')


