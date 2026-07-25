from django.shortcuts import render, redirect, get_object_or_404
from courses.models import GroupStudent
from courses.courses_forms.group_student_forms import GroupStudentsForms


def get_group_student(request):
    group_student = GroupStudent.objects.all()
    return render(request, 'courses/group_student/group_student_list.html', {'group_student': group_student})


def create_group_student(request):
    if request.method == 'POST':
        form = GroupStudentsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_student_list')
    else:
        form = GroupStudentsForms()
    return render(request, 'courses/group_student/create_group_student.html', {'form': form})


def read_group_student(request, pk):
    group_student = get_object_or_404(GroupStudent, pk=pk)
    return render(request, 'courses/group_student/read_group_student.html', {'group_student': group_student})


def update_group_student(request, pk):
    group_student = get_object_or_404(GroupStudent, pk=pk)
    if request.method == 'POST':
        form = GroupStudentsForms(request.POST, instance=group_student)
        if form.is_valid():
            form.save()
            return redirect('room_type_list')
    else:
        form = GroupStudentsForms(instance=group_student)
    return render(request, 'courses/group_student/update_group_student.html', {'form': form})


def delete_group_student(request, pk):
    group_student = get_object_or_404(GroupStudent, pk=pk)
    if request.method == 'POST':
        group_student.delete()
        return redirect('group_student_list')
    else:
        return render(request, 'courses/group_student/delete_group_student.html', {'group_student': group_student})
