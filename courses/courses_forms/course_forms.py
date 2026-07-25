from django import forms
from courses.models import Course

class CourseForms(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'duration_months', 'is_active']
