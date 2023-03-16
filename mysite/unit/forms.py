#Wanjala Stephen David
# IN16/00055/20

from django import forms
from .models import Unit

class NewUnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('code', 'title')


class EditUnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ('code', 'title')



