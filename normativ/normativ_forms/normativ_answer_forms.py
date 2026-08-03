from django import forms
from normativ.models import NormativAnswer

class NormativAnswerForm(forms.ModelForm):
    class Meta:
        model = NormativAnswer
        fields = ['answer_text']

class NormativAnswerAssessForm(forms.ModelForm):
    class Meta:
        model = NormativAnswer
        fields = ['score', 'feedback']