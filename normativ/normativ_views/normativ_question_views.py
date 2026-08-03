from django.shortcuts import render, redirect, get_object_or_404

from courses.models import Lesson
from normativ.models import NormativQuestion
from normativ.normativ_forms.normativ_question_forms import NormativQuestionForm


def get_normativ_question(request):
    questions = NormativQuestion.objects.all()
    return render(request, 'normativ/normativ_question/normativ_question_list.html', {'questions': questions})


def create_normativ_question(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = NormativQuestionForm(request.POST)
        if form.is_valid():
            normativ_question = form.save(commit=False)
            normativ_question.lesson = lesson
            normativ_question.save()
            return redirect('normativ_question_list')
    else:
        form = NormativQuestionForm()
    return render(request, 'normativ/normativ_question/create_normativ_question.html', {'form': form})


def read_normativ_question(request, pk):
    question = get_object_or_404(NormativQuestion, pk=pk)
    return render(request, 'normativ/normativ_question/read_normativ_question.html', {'question': question})


def update_normativ_question(request, pk):
    question = get_object_or_404(NormativQuestion, pk=pk)
    if request.method == 'POST':
        form = NormativQuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('normativ_question_list')
    else:
        form = NormativQuestionForm(instance=question)
    return render(request, 'normativ/normativ_question/update_normativ_question.html', {'form': form})


def delete_normativ_question(request, pk):
    question = get_object_or_404(NormativQuestion, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('normativ_question_list')
    return render(request, 'normativ/normativ_question/delete_normativ_question.html', {'question': question})
