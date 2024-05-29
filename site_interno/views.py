from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def operacional(request):
    return render(request, 'operacional.html')


def tecnico(request):
    return render(request, 'tecnico.html')


def condominio(request):
    return render(request, 'condominio.html')

def sobre(request):
    return render(request, 'sobre.html')
