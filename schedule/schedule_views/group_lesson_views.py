from django.shortcuts import render, redirect, get_object_or_404
from schedule.models import GroupLesson
from schedule.schedule_forms.group_lesson_forms import GroupLessonForm



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