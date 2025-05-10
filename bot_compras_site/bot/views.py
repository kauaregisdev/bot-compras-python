from django.shortcuts import render
from .scripts.main import execute # função que executa o bot

def iniciar(request):
    return render(request, 'bot/iniciar.html')

def resultado(request):
    if request.method == 'POST':
        produto = request.POST.get('produto')
        try:
            execute(produto)
        except Exception as e:
            print(f'Erro ao executar o bot: {e}')
            return render(request, 'bot/resultado.html', {'erro': 'Ocorreu um erro ao processar sua solicitação.'})
    return render(request, 'bot/resultado.html')