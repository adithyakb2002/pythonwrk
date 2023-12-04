from django import forms
from . models import Lemon

class Lemon_form(forms.ModelForm):
    class Meta:
        model=Lemon
        fields=['name']