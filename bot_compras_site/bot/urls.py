from django.urls import path
from . import views

urlpatterns = [
    path('comprar/', views.iniciar_compra, name='iniciar_compra'),
]