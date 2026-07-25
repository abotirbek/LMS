from django.shortcuts import render, redirect, get_object_or_404
from normativ.models import Normativ
from normativ.normativ_forms.normativ_forms import NormativForm



def get_normativ(request):
    normativ = Normativ.objects.all()
    return render(request, 'normativ/normativ/normativ_list.html', {'normativ': normativ})


def create_normativ(request):
    if request.method == 'POST':
        form = NormativForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('normativ_list')
    else:
        form = NormativForm()
    return render(request, 'normativ/normativ/create_normativ.html', {'form': form})


def read_normativ(request, pk):
    normativ = get_object_or_404(Normativ, pk=pk)
    return render(request, 'normativ/normativ/read_normativ.html', {'normativ': normativ})


def update_normativ(request, pk):
    normativ = get_object_or_404(Normativ, pk=pk)
    if request.method == 'POST':
        form = NormativForm(request.POST, instance=normativ)
        if form.is_valid():
            form.save()
            return redirect('normativ_list')
    else:
        form = NormativForm(instance=normativ)
    return render(request, 'normativ/normativ/update_normativ.html', {'form': form})


def delete_normativ(request, pk):
    normativ = get_object_or_404(Normativ, pk=pk)
    if request.method == 'POST':
        normativ.delete()
        return redirect('normativ_list')
    return render(request, 'normativ/normativ/delete_normativ.html', {'normativ': normativ})
