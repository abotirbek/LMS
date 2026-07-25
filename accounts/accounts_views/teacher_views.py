from django.shortcuts import render, redirect
from accounts.accounts_forms.teacher_forms import TeacherForm
from accounts.models import TeacherProfile


def get_teacher_profile(request):
    user = request.user
    if user:
        profile = TeacherProfile.objects.get(user=user)
    else:
        return redirect('base.html')
    return render(request, 'accounts/registration/profile.hmtl', {'profile': profile})

def edit_teacher_profile(request):
    profile = TeacherProfile.objects.get(user=request.user)
    user = request.user

    if request.method == "POST":
        form = TeacherForm(
            request.POST,
            request.FILES,
            user_instance=user,
            profile_instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("teacher_profile")

    else:
        form = TeacherForm(
            user_instance=user,
            profile_instance=profile
        )

    return render(request, 'accounts/edit_profile/profile.hmtl', {'form': form})


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