from django import forms
from normativ.models import Normativ

class NormativForm(forms.ModelForm):
    class Meta:
        model = Normativ
        fields = ['lesson', 'title', 'description']