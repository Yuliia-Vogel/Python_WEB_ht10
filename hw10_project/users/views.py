# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate as auth_auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('quote_list') # куди перекидає при натисканні кнопки "зареєструватися"
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('quote_list')  # куди перекидає при натисканні кнопки "залогінитися"
#     else:
#         form = AuthenticationForm()
#     return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('quote_list') # куди перекидає при натисканні кнопки "розлогінитися"
    return render(request, 'users/logout.html') 


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, "You logged in successfully!")
            return redirect('quote_list')
        else:
            messages.error(request, "Login error. Please try again.")
    else:
        messages.info(request, "Enter the system please. Registered users only can add new authors and quotes.")
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})