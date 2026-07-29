from django import forms
from courses.models import Lesson

class LessonForms(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'order', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }