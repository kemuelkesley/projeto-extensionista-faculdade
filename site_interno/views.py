from django.shortcuts import render
from .models import Operacional, Categoria, Tecnico, Condominio ,Sobre


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
    condominios = Condominio.objects.all()

    context = {
        'condominios': condominios
    }

    return render(request, 'condominio.html', context)


def sobre(request):
    sobre = Sobre.objects.all()
    
    context = {
        'sobre': sobre
    }
    return render(request, 'sobre.html', context)
