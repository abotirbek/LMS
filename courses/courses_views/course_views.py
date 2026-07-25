from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course
from courses.courses_forms.course_forms import CourseForms

# Create your accounts_views here.


def get_course(request):
    course = Course.objects.all()
    return render(request, 'courses/course/course_list.html', {'course': course})


def create_course(request):
    if request.method == 'POST':
        form = CourseForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForms()
    return render(request, 'courses/course/create_course.html', {'form': form})


def read_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course/read_course.html', {'course': course})


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForms(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForms(instance=course)
    return render(request, 'courses/course/update_course.html', {'form': form})


def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    else:
        return render(request, 'courses/course/delete_course.html', {'course': course})