from django.urls import path
from App1.views import *

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('equipos', equipos, name = 'Equipos'),
    path('categorias', categorias, name = 'Categorias'),
    path('busqueda-equipos', busqueda_equipos, name = 'Buscar Equipos'),
    path( 'buscar', buscar_equipos, name='Buscar'),
    path( 'formulario-clubes', crear_equipos, name='Formulario de Clubes'),
    
]