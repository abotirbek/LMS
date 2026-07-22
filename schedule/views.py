from django.shortcuts import render, redirect, get_object_or_404
from .models import GroupSchedule, GroupLesson
from .forms import GroupScheduleForm, GroupLessonForm

def get_group_schedule(request):
    group_schedule = GroupSchedule.objects.all()
    return render(request, 'schedule/group_schedule/group_schedule_list.html', {'group_schedule': group_schedule})

def create_group_schedule(request):
    if request.method == 'POST':
        form = GroupScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_schedule_list')
    else:
        form = GroupScheduleForm()
    return render(request, 'schedule/group_schedule/create_group_schedule.html', {'form': form})

def read_group_schedule(request, pk):
    group_schedule = get_object_or_404(GroupSchedule, pk=pk)
    return render(request, 'schedule/group_schedule/read_group_schedule.html', {'group_schedule': group_schedule})

def update_group_schedule(request, pk):
    group_schedule = get_object_or_404(GroupSchedule, pk=pk)
    if request.method == 'POST':
        form = GroupScheduleForm(request.POST, instance=group_schedule)
        if form.is_valid():
            form.save()
            return redirect('group_schedule_list')
    else:
        form = GroupScheduleForm(instance=group_schedule)
    return render(request, 'schedule/group_schedule/update_group_schedule.html', {'form': form})

def delete_group_schedule(request, pk):
    group_schedule = get_object_or_404(GroupSchedule, pk=pk)
    if request.method == 'POST':
        group_schedule.delete()
        return redirect('group_schedule_list')
    return render(request, 'schedule/group_schedule/delete_group_schedule.html', {'group_schedule': group_schedule})

def get_group_lesson(request):
    group_lesson = GroupLesson.objects.all()
    return render(request, 'schedule/group_lesson/group_lesson_list.html', {'group_lesson': group_lesson})

def create_group_lesson(request):
    if request.method == 'POST':
        form = GroupLessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_lesson_list')
    else:
        form = GroupLessonForm()
    return render(request, 'schedule/group_lesson/create_group_lesson.html', {'form': form})

def read_group_lesson(request, pk):
    group_lesson = get_object_or_404(GroupLesson, pk=pk)
    return render(request, 'schedule/group_lesson/read_group_lesson.html', {'group_lesson': group_lesson})

def update_group_lesson(request, pk):
    group_lesson = get_object_or_404(GroupLesson, pk=pk)
    if request.method == 'POST':
        form = GroupLessonForm(request.POST, instance=group_lesson)
        if form.is_valid():
            form.save()
            return redirect('group_lesson_list')
    else:
        form = GroupLessonForm(instance=group_lesson)
    return render(request, 'schedule/group_lesson/update_group_lesson.html', {'form': form})

def delete_group_lesson(request, pk):
    group_lesson = get_object_or_404(GroupLesson, pk=pk)
    if request.method == 'POST':
        group_lesson.delete()
        return redirect('group_lesson_list')
    return render(request, 'schedule/group_lesson/delete_group_lesson.html', {'group_lesson': group_lesson})