from django import forms
from courses.models import Room

class RoomForms(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity']