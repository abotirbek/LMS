from django import forms
from courses.models import Groups

class GroupForms(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['course', 'teacher', 'mentor', 'name', 'start_date', 'is_active']