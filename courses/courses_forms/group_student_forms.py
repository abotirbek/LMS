from django import forms
from courses.models import GroupStudent

class GroupStudentsForms(forms.ModelForm):
    class Meta:
        model = GroupStudent
        fields = ['groups', 'student', 'is_active']