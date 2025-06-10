from django.urls import path
from . import views  # Импорт ваших views


app_name = 'dictionary'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.term_search, name='term_search'),
    path('legal/', views.legal, name='legal'),
    path('supply-chain/', views.supply_chain, name='supply_chain'),
    path('terms/dpas/', views.term_dpas, name='term_dpas'),
]