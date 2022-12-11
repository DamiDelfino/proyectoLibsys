from django.urls import path
from . views import (index, registro, loginUser, plastas, abrazoArbol, ninasRebeldes, buscaLibros)

urlpatterns = [
    path("", index, name="index"),
    path('login/', loginUser, name='login'),
    path('registro/', registro, name='registro'),
    path("plastas/", plastas, name="plastas"),
    path("abrazoArbol/", abrazoArbol, name="abrazoArbol"),
    path("ninasRebeldes/", ninasRebeldes, name="ninasRebeldes"),
    path("buscaLibros/", buscaLibros, name="buscaLibros"),
    
]

