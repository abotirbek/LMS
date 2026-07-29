from django import forms
from schedule.models import GroupSchedule

# class GroupScheduleForm(forms.ModelForm):
#     class Meta:
#         model = GroupSchedule
#         fields = ['group', 'weekday', 'start_time', 'end_time', 'room']

class GroupScheduleForm(forms.ModelForm):
    class Meta:
        model = GroupSchedule
        fields = ['weekday', 'start_time', 'end_time', 'room']