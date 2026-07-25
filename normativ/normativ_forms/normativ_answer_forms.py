from django import forms
from normativ.models import NormativAnswer

class NormativAnswerForm(forms.ModelForm):
    class Meta:
        model = NormativAnswer
        fields = ['question', 'student', 'answer_text', 'score', 'feedback', 'checked_by', 'checked_at']