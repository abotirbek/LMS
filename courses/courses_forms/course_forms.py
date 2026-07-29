from django import forms
from courses.models import Course

class CourseForms(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'duration_months', 'is_active']

    def clean_duration_months(self):
        value = self.cleaned_data['duration_months']
        if not 1 <= value <= 24:
            raise forms.ValidationError("Davomiylik 1-24 oy oralig'ida bo'lishi kerak")
        return value
