from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def calculadora_imc(request):
    return render(request, 'calculadora_imc.html')
