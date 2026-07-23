from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, TeacherForm, StudentForm
from .models import StudentProfile, TeacherProfile, CustomUser
from django.contrib.auth import authenticate, login, logout
from .roles import role_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            StudentProfile.objects.create(user = user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = LoginForm()
    return render(request, 'accounts/registration/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

@role_required('teacher')
def get_teacher_profile(request):
    user = request.user
    if user:
        profile = TeacherProfile.objects.get(user=user)
    else:
        return redirect('base.html')
    return render(request, 'accounts/registration/profile.hmtl', {'profile': profile})

@role_required('teacher')
def edit_teacher_profile(request):
    teacher_profile = None
    user = request.user
    if user:
        teacher_profile = TeacherProfile.objects.get(user=user)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher_profile)
        if form.is_valid():
            form.save()
            return redirect('teacher_profile')
    else:
        form = TeacherForm(instance=teacher_profile)
    return render(request, 'accounts/edit_profile/profile.hmtl', {'form': form})

@role_required('student')
def get_student_profile(request):
    user = request.user
    if user:
        profile = StudentProfile.objects.get(user=user)
    else:
        return redirect('base.html')
    return render(request, 'accounts/registration/profile.html', {'profile': profile})

@role_required('student')
def edit_student_profile(request):
    student_profile = None
    user = request.user
    if user:
        student_profile = StudentProfile.objects.get(user=user)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student_profile)
        if form.is_valid():
            form.save()
            return redirect('student_profile')
    else:
        form = StudentForm(instance=student_profile)
    return render(request, 'accounts/registration/edit_profile.html', {'form': form})

def show_home(request):
    return render(request, 'base.html')

def get_student_base(request):
    user = request.user
    if user:
        student_base = StudentProfile.objects.get(user=user)
    else:
        return redirect('base.html')
    return render(request, 'student_base.html', {'student_base': student_base})

def get_teacher_base(request):
    user = request.user
    if user:
        teacher_base = TeacherProfile.objects.get(user=user)
    else:
        return redirect('base.html')
    return render(request, 'student_base.html', {'teacher_base': teacher_base})

def get_teacher(request):
    teacher = TeacherProfile.objects.all()
    return render(request, 'accounts/teacher/teacher_list.html', {'teacher': teacher})

def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'accounts/teacher/create_teacher.html', {'form': form})

def read_teacher(request, pk):
    teacher = get_object_or_404(TeacherProfile, pk=pk)
    return render(request, 'accounts/teacher/read_teacher.html', {'teacher': teacher})

def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'accounts/teacher/update_teacher.html', {'form': form})

def delete_teacher(request, pk):
    teacher = get_object_or_404(TeacherProfile, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'accounts/teacher/delete_teacher.html', {'teacher': teacher})

# Student --- CRUD

def get_student(request):
    student = StudentProfile.objects.all()
    return render(request, 'accounts/student/student_list.html', {'student': student})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'accounts/student/create_student.html', {'form': form})

def read_student(request, pk):
    student = get_object_or_404(StudentProfile, pk=pk)
    return render(request, 'accounts/student/read_student.html', {'student': student})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'accounts/student/update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(StudentProfile, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'accounts/student/delete_student.html', {'student': student})