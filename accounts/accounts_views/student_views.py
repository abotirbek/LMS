from django.shortcuts import render, redirect
from accounts.accounts_forms.student_forms import StudentForm
from accounts.models import StudentProfile

def get_student_profile(request):
    user = request.user
    if user:
        profile = StudentProfile.objects.get(user=user)
    else:
        return redirect('base.html')
    return render(request, 'accounts/registration/profile.html', {'profile': profile})

def edit_student_profile(request):
    profile = StudentProfile.objects.get(user=request.user)
    user = request.user

    if request.method == "POST":
        form = StudentForm(
            request.POST,
            request.FILES,
            user_instance=user,
            profile_instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("student_profile")

    else:
        form = StudentForm(
            user_instance=user,
            profile_instance=profile
        )

    return render(
        request,
        "accounts/registration/edit_profile.html",
        {"form": form}
    )


def get_student_base(request):
    user = request.user
    if user:
        student_base = StudentProfile.objects.get(user=user)
    else:
        return redirect('base.html')
    return render(request, 'student_base.html', {'student_base': student_base})


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