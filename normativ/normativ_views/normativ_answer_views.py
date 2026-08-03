from enum import member

from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import StudentProfile
from normativ.models import NormativAnswer, NormativQuestion
from normativ.normativ_forms.normativ_answer_forms import NormativAnswerForm, NormativAnswerAssessForm


def get_normativ_answer(request):
    questions = NormativQuestion.objects.filter(lesson__module__course__groups__memberships__student = request.user.student_profile).distinct()
    answers = NormativAnswer.objects.all()
    conetxt = {
        'questions': questions,
        'answers': answers
    }
    return render(request, 'normativ/normativ_answer/normativ_answer_list.html', conetxt)


def create_normativ_answer(request, pk):
    normativ_question = get_object_or_404(NormativQuestion, pk=pk)
    if request.method == 'POST':
        form = NormativAnswerForm(request.POST)
        if form.is_valid():
            normativ_answer = form.save(commit=False)
            normativ_answer.student = request.user.student_profile
            normativ_answer.question = normativ_question
            normativ_answer.save()
            return redirect('normativ_answer_list')
    else:
        form = NormativAnswerForm()
    context = {
        'normativ_question': normativ_question,
        'form': form
    }
    return render(request, 'normativ/normativ_answer/create_normativ_answer.html', context)


def read_normativ_answer(request, pk):
    answer = get_object_or_404(NormativAnswer, pk=pk)
    return render(request, 'normativ/normativ_answer/read_normativ_answer.html', {'answer': answer})


def update_normativ_answer(request, pk):
    answer = get_object_or_404(NormativAnswer, pk=pk)
    if request.method == 'POST':
        form = NormativAnswerAssessForm(request.POST, instance=answer)
        if form.is_valid():
            answer.checked_by = request.user
            answer.save()
            form.save()
            return redirect('check_normativs')
    else:
        form = NormativAnswerAssessForm(instance=answer)
    return render(request, 'normativ/normativ_answer/update_normativ_answer.html', {'form': form})

def delete_normativ_answer(request, pk):
    answer = get_object_or_404(NormativAnswer, pk=pk)
    if request.method == 'POST':
        answer.delete()
        return redirect('normativ_answer_list')
    return render(request, 'normativ/normativ_answer/delete_normativ_answer.html', {'answer': answer})

def check_normativs(request):
    if request.user.role == 'teacher':
        students = StudentProfile.objects.filter(memberships__groups__teacher = request.user.teacher_profile).distinct()
    return render(request, 'normativ/normativ_answer/check_normativs.html', {'students': students})

def check_students_normativs(request, pk):
    if request.user.role == 'teacher':
        student = get_object_or_404(StudentProfile, pk=pk)
        answers = student.normativ_answers.all()
    else:
        student = None
        answers = None
    context = {
        'student': student,
        'answers': answers,
    }
    return render(request, 'normativ/normativ_answer/check_students_normativs.html', context)