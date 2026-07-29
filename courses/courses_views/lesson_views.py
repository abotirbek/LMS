from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Lesson
from courses.courses_forms.lesson_forms import LessonForms
from courses.models import Groups, Module


def get_lesson(request):
    lesson = Lesson.objects.all()
    return render(request, 'courses/lesson/lesson_list.html', {'lesson': lesson})


def create_lesson(request, groups_pk, module_pk):
    groups = get_object_or_404(Groups, pk=groups_pk)
    module = get_object_or_404(Module, pk=module_pk)
    if request.method == 'POST':
        form = LessonForms(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.group = groups
            lesson.module = module
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForms()
    return render(request, 'courses/lesson/create_lesson.html', {'form': form})


def read_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'courses/lesson/read_lesson.html', {'lesson': lesson})


def update_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForms(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForms(instance=lesson)
    return render(request, 'courses/lesson/update_lesson.html', {'form': form})


def delete_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        lesson.delete()
        return redirect('lesson_list')
    else:
        return render(request, 'courses/lesson/delete_lesson.html', {'lesson': lesson})