from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Module
from courses.courses_forms.module_forms import ModuleForms
from courses.models import Course



def get_module(request):
    module = Module.objects.all()
    return render(request, 'courses/module/module_list.html', {'module': module})


def create_module(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = ModuleForms(request.POST)
        if form.is_valid():
            module = form.save(commit=False)
            module.course = course
            module.save()
            return redirect('read_course', course.pk)
    else:
        form = ModuleForms()
    context = {'form': form, 'course': course,}
    return render(request, 'courses/module/create_module.html', context)


def read_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    return render(request, 'courses/module/read_module.html', {'module': module})


def update_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    if request.method == 'POST':
        form = ModuleForms(request.POST, request.FILES, instance=module)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = ModuleForms(instance=module)
    return render(request, 'courses/module/update_module.html', {'form': form})


def delete_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    if request.method == 'POST':
        module.delete()
        return redirect('module_list')
    else:
        return render(request, 'courses/module/delete_module.html', {'module': module})
