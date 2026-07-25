from django.shortcuts import render, redirect
from accounts.accounts_forms.registration_forms import RegistrationForm, LoginForm
from accounts.models import StudentProfile
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            StudentProfile.objects.create(user = user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = LoginForm()
    return render(request, 'accounts/registration/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')


def show_home(request):
    return render(request, 'base.html')