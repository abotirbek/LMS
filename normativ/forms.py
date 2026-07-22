from django import forms
from .models import Normativ, NormativQuestion, NormativAnswer

class NormativForm(forms.ModelForm):
    class Meta:
        model = Normativ
        fields = ['lesson', 'title', 'description']

class NormativQuestionForm(forms.ModelForm):
    class Meta:
        model = NormativQuestion
        fields = ['normativ', 'text', 'max_score', 'order']

class NormativAnswerForm(forms.ModelForm):
    class Meta:
        model = NormativAnswer
        fields = ['question', 'student', 'answer_text', 'score', 'feedback', 'checked_by', 'checked_at']