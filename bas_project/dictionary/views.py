from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import DroneTerm, Favorite, Language
from .forms import SearchForm


def term_detail(request, term_id):
    term = get_object_or_404(DroneTerm, pk=term_id)
    source_lang = request.GET.get('source_lang', 'ru')
    target_lang = request.GET.get('target_lang', 'en')
    return render(request, 'pages/term-detail.html', {
        'term': term,
        'source_lang': source_lang,
        'target_lang': target_lang
    })


def term_search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            source_lang = request.GET.get('source_lang', 'ru')
            target_lang = request.GET.get('target_lang', 'en')

            if source_lang == 'ru':
                term = DroneTerm.objects.filter(term_rus__iexact=query).first()
            else:
                term = DroneTerm.objects.filter(term_eng__iexact=query).first()

            if term:
                # сохраняем в историю
                if request.user.is_authenticated:
                    from .models import SearchHistory
                    SearchHistory.objects.create(user=request.user, term=term, query=query)

                return render(request, 'pages/term-dpas.html', {
                    'term': term,
                    'source_lang': source_lang,
                    'target_lang': target_lang
                })
            else:
                messages.error(request, 'Термин не найден')
    else:
        form = SearchForm()
        
    return render(request, 'pages/term-dpas.html', {'form': form})


def home(request):
    template_name = 'pages/home.html'
    return render(request, template_name)


def legal(request):
    return render(request, 'pages/legal.html')


def supply_chain(request):
    return render(request, 'pages/supply_chain.html')


def term_dpas(request):
    return render(request, 'pages/term-dpas.html')


@login_required
def add_to_favorites(request, term_id):
    term = get_object_or_404(DroneTerm, pk=term_id)
    Favorite.objects.get_or_create(user=request.user, term=term)
    return redirect('dictionary:term_dpas', term_id=term.id)