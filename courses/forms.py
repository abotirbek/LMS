from django import forms
from .models import Room, Course, Module, Lesson, Groups, GroupStudent

class RoomForms(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity']

class CourseForms(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'duration_months', 'is_active']

class ModuleForms(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['course', 'title', 'order']

class LessonForms(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['module', 'title', 'content', 'order']

class GroupForms(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ['course', 'teacher', 'mentor', 'name', 'start_date', 'is_active', 'students']

class GroupStudentsForms(forms.ModelForm):
    class Meta:
        model = GroupStudent
        fields = ['groups', 'student', 'joined_at', 'left_at', 'is_active']