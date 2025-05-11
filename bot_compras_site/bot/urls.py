from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar, name='iniciar'),
    path('resultado/', views.resultado, name='resultado'),
]