from django.shortcuts import render
from .models import Operacional, Categoria, Tecnico ,Sobre


def index(request):
    return render(request, 'index.html')


def operacional(request):
    operacional = Operacional.objects.all()

    context = {
        'operacional': operacional
    }

    return render(request, 'operacional.html', context)


def tecnico(request):
    tecnico = Tecnico.objects.all()
    categorias = Categoria.objects.all()

    context = {
        'tecnico': tecnico,
        'categorias': categorias
    }

    return render(request, 'tecnico.html', context)


def condominio(request):
    return render(request, 'condominio.html')


def sobre(request):
    sobre = Sobre.objects.all()
    
    context = {
        'sobre': sobre
    }
    return render(request, 'sobre.html', context)
