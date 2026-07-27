from django import forms
from courses.models import Module

class ModuleForms(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'order']