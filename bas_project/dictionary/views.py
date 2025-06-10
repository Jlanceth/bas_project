from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import DroneTerm
from .forms import SearchForm


def term_search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            terms = DroneTerm.objects.filter(term__icontains=query)
            return render(request, 'pages/search.html', {'terms': terms})
    else:
        form = SearchForm()
    return render(request, 'pages/search.html', {'form': form})


def home(request):
    template_name = 'pages/home.html'
    return render(request, template_name)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверный логин или пароль')

    return render(request, 'auth/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def forgot_password(request):
    # Логика восстановления пароля
    return render(request, 'auth/forgot_password.html')


def legal(request):
    return render(request, 'pages/legal.html')


def supply_chain(request):
    return render(request, 'pages/supply_chain.html')


def term_dpas(request):
    return render(request, 'pages/term-dpas.html')


def my_dictionary(request):
    return render(request, 'pages/my_dictionary.html')


def history(request):
    return render(request, 'pages/history.html')
