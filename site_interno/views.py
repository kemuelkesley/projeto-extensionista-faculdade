from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Operacional, Categoria, Tecnico, Condominio ,Sobre


def index(request):
    condominios = Condominio.objects.all()
    paginator = Paginator(condominios, 5) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    return render(request, "index.html", {"page_obj": page_obj, "condominios": condominios})


def listar(request):
    lista_condominios = Condominio.objects.all()
    paginator = Paginator(lista_condominios, 5)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", {"page_obj": page_obj})



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


