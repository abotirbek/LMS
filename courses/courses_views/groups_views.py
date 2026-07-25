from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Groups
from courses.courses_forms.groups_forms import GroupForms

# Create your accounts_views here.

def get_group(request):
    groups = Groups.objects.all()
    return render(request, 'courses/groups/groups_list.html', {'groups': groups})


def create_group(request):
    if request.method == 'POST':
        form = GroupForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups_list')
    else:
        form = GroupForms()
    return render(request, 'courses/groups/create_groups.html', {'form': form})


def read_group(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    return render(request, 'courses/groups/read_groups.html', {'groups': groups})


def update_group(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    if request.method == 'POST':
        form = GroupForms(request.POST, instance=groups)
        if form.is_valid():
            form.save()
            return redirect('groups_list')
    else:
        form = GroupForms(instance=groups)
    return render(request, 'courses/groups/update_groups.html', {'form': form})


def delete_group(request, pk):
    groups = get_object_or_404(Groups, pk=pk)
    if request.method == 'POST':
        groups.delete()
        return redirect('groups_list')
    else:
        return render(request, 'courses/groups/delete_groups.html', {'groups': groups})