from django import forms
from normativ.models import NormativQuestion

class NormativQuestionForm(forms.ModelForm):
    class Meta:
        model = NormativQuestion
        fields = ['normativ', 'text', 'max_score', 'order']