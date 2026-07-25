from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Room
from courses.courses_forms.room_forms import RoomForms



def get_room(request):
    room = Room.objects.all()
    return render(request, 'courses/room/room_list.html', {'room': room})


def create_room(request):
    if request.method == 'POST':
        form = RoomForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForms()
    return render(request, 'courses/room/create_room.html', {'form': form})


def read_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'courses/room/read_room.html', {'room': room})


def update_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForms(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForms(instance=room)
    return render(request, 'courses/room/update_room.html', {'form': form})

def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    else:
        return render(request, 'courses/room/delete_room.html', {'room': room})
