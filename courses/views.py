from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Course, Module, Lesson, Groups, GroupStudent
from .forms import RoomForms, CourseForms, ModuleForms, LessonForms, GroupForms, GroupStudentsForms

# Create your views here.

# COURSE --- CRUD

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
    return render(request, 'education/course/create_course.html', {'form': form})

def read_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'education/course/read_course.html', {'course': course})

def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForms(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForms(instance=course)
    return render(request, 'education/course/update_course.html', {'form': form})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    else:
        return render(request, 'education/course/delete_course.html', {'course': course})

# GROUP --- CRUD

def get_group(request):
    groups = Groups.objects.all()
    return render(request, 'education/groups/groups_list.html', {'groups': groups})

def create_group(request):
    if request.method == 'POST':
        form = GroupForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups_list')
    else:
        form = GroupForms()
    return render(request, 'education/groups/create_groups.html', {'form': form})

def read_group(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    return render(request, 'education/groups/read_groups.html', {'groups': groups})

def update_group(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    if request.method == 'POST':
        form = GroupForms(request.POST, instance=groups)
        if form.is_valid():
            form.save()
            return redirect('groups_list')
    else:
        form = GroupForms(instance=groups)
    return render(request, 'education/groups/update_groups.html', {'form': form})

def delete_group(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    if request.method == 'POST':
        groups.delete()
        return redirect('groups_list')
    else:
        return render(request, 'education/groups/delete_groups.html', {'groups': groups})

# MODULE --- CRUD

def get_module(request):
    module = Module.objects.all()
    return render(request, 'lesson/module/module_list.html', {'module': module})

def create_module(request):
    if request.method == 'POST':
        form = ModuleForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = ModuleForms()
    return render(request, 'lesson/module/create_module.html', {'form': form})

def read_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    return render(request, 'lesson/module/read_module.html', {'module': module})

def update_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    if request.method == 'POST':
        form = ModuleForms(request.POST, request.FILES, instance=module)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = ModuleForms(instance=module)
    return render(request, 'lesson/module/update_module.html', {'form': form})

def delete_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    if request.method == 'POST':
        module.delete()
        return redirect('module_list')
    else:
        return render(request, 'lesson/module/delete_module.html', {'module': module})


# GROUP STUDENT --- CRUD

def get_group_student(request):
    group_student = GroupStudent.objects.all()
    return render(request, 'lesson/group_student/group_student_list.html', {'group_student': group_student})

def create_group_student(request):
    if request.method == 'POST':
        form = GroupStudentsForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_student_list')
    else:
        form = GroupStudentsForms()
    return render(request, 'lesson/group_student/create_group_student.html', {'form': form})

def read_group_student(request, pk):
    group_student = get_object_or_404(GroupStudent, pk=pk)
    return render(request, 'lesson/group_student/read_group_student.html', {'group_student': group_student})

def update_group_student(request, pk):
    group_student = get_object_or_404(GroupStudent, pk=pk)
    if request.method == 'POST':
        form = GroupStudentsForms(request.POST, instance=group_student)
        if form.is_valid():
            form.save()
            return redirect('room_type_list')
    else:
        form = GroupStudentsForms(instance=group_student)
    return render(request, 'lesson/group_student/update_group_student.html', {'form': form})

def delete_group_student(request, pk):
    group_student = get_object_or_404(GroupStudent, pk=pk)
    if request.method == 'POST':
        group_student.delete()
        return redirect('group_student_list')
    else:
        return render(request, 'lesson/group_student/delete_group_student.html', {'group_student': group_student})

# ROOM --- CRUD

def get_room(request):
    room = Room.objects.all()
    return render(request, 'lesson/room/room_list.html', {'room': room})


def create_room(request):
    if request.method == 'POST':
        form = RoomForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForms()
    return render(request, 'lesson/room/create_room.html', {'form': form})


def read_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'lesson/room/read_room.html', {'room': room})


def update_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForms(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForms(instance=room)
    return render(request, 'lesson/room/update_room.html', {'form': form})

def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    else:
        return render(request, 'lesson/room/delete_room.html', {'room': room})


# LESSON --- CRUD

def get_lesson(request):
    lesson = Lesson.objects.all()
    return render(request, 'lesson/lesson/lesson_list.html', {'lesson': lesson})

def create_lesson(request):
    if request.method == 'POST':
        form = LessonForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForms()
    return render(request, 'lesson/lesson/create_lesson.html', {'form': form})

def read_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lesson/lesson/read_lesson.html', {'lesson': lesson})

def update_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForms(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForms(instance=lesson)
    return render(request, 'lesson/lesson/update_lesson.html', {'form': form})

def delete_lesson(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        lesson.delete()
        return redirect('lesson_list')
    else:
        return render(request, 'lesson/lesson/delete_lesson.html', {'lesson': lesson})