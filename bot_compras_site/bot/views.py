from django.shortcuts import render
from .scripts.main import execute # função que executa o bot

def iniciar_compra(request):
    if request.method == 'POST':
        resultado = execute()
        return render(request, "bot/resultado.html", {"resultado": resultado})
    return render(request, "bot/iniciar.html")