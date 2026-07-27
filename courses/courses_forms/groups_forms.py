from django import forms
from courses.models import Groups

class GroupForms(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name', 'course', 'teacher', 'students', 'mentor', 'start_date', 'is_active']
        widgets = {
            'students': forms.CheckboxSelectMultiple(),
        }