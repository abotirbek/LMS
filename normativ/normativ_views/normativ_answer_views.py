from django.shortcuts import render, redirect, get_object_or_404
from normativ.models import NormativAnswer
from normativ.normativ_forms.normativ_answer_forms import NormativAnswerForm



def get_normativ_answer(request):
    answers = NormativAnswer.objects.all()
    return render(request, 'normativ/normativ_answer/normativ_answer_list.html', {'answers': answers})


def create_normativ_answer(request):
    if request.method == 'POST':
        form = NormativAnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('normativ_answer_list')
    else:
        form = NormativAnswerForm()
    return render(request, 'normativ/normativ_answer/create_normativ_answer.html', {'form': form})


def read_normativ_answer(request, pk):
    answer = get_object_or_404(NormativAnswer, pk=pk)
    return render(request, 'normativ/normativ_answer/read_normativ_answer.html', {'answer': answer})


def update_normativ_answer(request, pk):
    answer = get_object_or_404(NormativAnswer, pk=pk)
    if request.method == 'POST':
        form = NormativAnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return redirect('normativ_answer_list')
    else:
        form = NormativAnswerForm(instance=answer)
    return render(request, 'normativ/normativ_answer/update_normativ_answer.html', {'form': form})


def delete_normativ_answer(request, pk):
    answer = get_object_or_404(NormativAnswer, pk=pk)
    if request.method == 'POST':
        answer.delete()
        return redirect('normativ_answer_list')
    return render(request, 'normativ/normativ_answer/delete_normativ_answer.html', {'answer': answer})