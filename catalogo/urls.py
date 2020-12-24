from django.urls import path
from .views import index, mostra_fotos

urlpatterns = [
    path('', index, name='index'),
    path('catalogo', mostra_fotos, name='mostra_fotos'),
]