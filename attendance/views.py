from django.shortcuts import render, redirect, get_object_or_404
from .models import Attendance
from .forms import AttendanceForm


def get_attendance(request):
    attendance = Attendance.objects.all()
    return render(request, 'attendance/attendance/attendance_list.html', {'attendance': attendance})


def create_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/attendance/create_attendance.html', {'form': form})


def read_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    return render(request, 'attendance/attendance/read_attendance.html', {'attendance': attendance})


def update_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'attendance/attendance/update_attendance.html', {'form': form})


def delete_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'attendance/attendance/delete_attendance.html', {'attendance': attendance})
