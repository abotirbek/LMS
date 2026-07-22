from django import forms
from .models import GroupSchedule, GroupLesson

class GroupScheduleForm(forms.ModelForm):
    class Meta:
        model = GroupSchedule
        fields = ['group', 'weekday', 'start_time', 'end_time', 'room']

class GroupLessonForm(forms.ModelForm):
    class Meta:
        model = GroupLesson
        fields = ['group', 'lesson', 'date', 'teacher']