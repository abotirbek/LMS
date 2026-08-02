from django import forms
from normativ.models import NormativQuestion

class NormativQuestionForm(forms.ModelForm):
    class Meta:
        model = NormativQuestion
        fields = ['text', 'max_score', 'order']