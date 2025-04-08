from django.shortcuts import render, get_object_or_404
from .models import DroneTerm
from .forms import SearchForm

def term_search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            terms = DroneTerm.objects.filter(term__icontains=query)
            return render(request, 'dictionary/search.html', {'terms': terms})
    else:
        form = SearchForm()
    return render(request, 'dictionary/search.html', {'form': form})