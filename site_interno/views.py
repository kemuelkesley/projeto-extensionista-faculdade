from django.shortcuts import render
from .models import Operacional


def index(request):
    return render(request, 'index.html')


def operacional(request):
    operacional = Operacional.objects.all()

    context = {
        'operacional': operacional
    }

    return render(request, 'operacional.html', context)


def tecnico(request):
    return render(request, 'tecnico.html')


def condominio(request):
    return render(request, 'condominio.html')

def sobre(request):
    return render(request, 'sobre.html')
