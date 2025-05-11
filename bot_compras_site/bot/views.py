from django.shortcuts import render
from .scripts.main import execute # função que executa o bot

def iniciar(request):
    return render(request, 'bot/iniciar.html')

def resultado(request):
    return render(request, 'bot/resultado.html')