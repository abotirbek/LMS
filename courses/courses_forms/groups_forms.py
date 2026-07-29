from django import forms
from courses.models import Groups

class GroupForms(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['name', 'course', 'teacher', 'students', 'mentor', 'start_date', 'is_active']
        widgets = {
            'students': forms.CheckboxSelectMultiple(),
        }

class GroupStudentForms(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['students']
        widgets = {
            'students': forms.CheckboxSelectMultiple(),
        }