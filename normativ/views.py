from django.shortcuts import render, redirect, get_object_or_404
from .models import Normativ, NormativQuestion, NormativAnswer
from .forms import NormativForm, NormativQuestionForm, NormativAnswerForm


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


def get_normativ_question(request):
    questions = NormativQuestion.objects.all()
    return render(request, 'normativ/normativ_question/normativ_question_list.html', {'questions': questions})


def create_normativ_question(request):
    if request.method == 'POST':
        form = NormativQuestionForm(request.POST)
        if form.is_valid():
            form.save()
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
