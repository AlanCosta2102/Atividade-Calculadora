from django.urls import path
from .views import home, calculadora_imc

urlpatterns = [
    path('', home, name='home'),
    path('calculadora/', calculadora_imc, name='calculadora_imc'),
]
