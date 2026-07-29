from django import forms
from schedule.models import GroupLesson

class GroupLessonForm(forms.ModelForm):
    class Meta:
        model = GroupLesson
        fields = ['group', 'lesson', 'teacher']