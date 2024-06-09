from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Operacional, Categoria, Tecnico, Condominio ,Sobre
# Importando a função de busca no banco de dados
from .sql import buscar_condominios
# Importando a função de paginação
from .metodos_genericos import criar_paginacao



def index(request):
    search_value = request.GET.get('q', '').strip()
    
    # Use a função de busca para obter os resultados filtrados
    condominios = buscar_condominios(search_value)
    
    
    paginas = criar_paginacao(request, condominios, 5)
    page_obj = paginas

    context = {
        "page_obj": page_obj,
        "search_value": search_value,
        "no_results": not condominios.exists()
    }

    return render(request, "index.html", context)


def operacional(request):
    operacional = Operacional.objects.filter(activate=True)
    paginas = criar_paginacao(request, operacional, 4)

    page_obj = paginas

    return render(request, 'operacional.html', {"page_obj": page_obj, "operacional": operacional})


def tecnico(request):
    tecnico = Tecnico.objects.filter(activate=True)
    categorias = Categoria.objects.filter(activate=True)

    paginator = Paginator(categorias, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request, 'tecnico.html', {"page_obj": page_obj, "tecnico": tecnico, "categorias": categorias})


def condominio(request):
    condominios = Condominio.objects.filter(activate=True)
    paginator = Paginator(condominios, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

   
    return render(request, 'condominio.html', {"page_obj": page_obj, "condominios": condominios})


def sobre(request):
    sobre = Sobre.objects.filter(activate=True)
    
    context = {
        'sobre': sobre
    }
    return render(request, 'sobre.html', context)


# Criando a função de paginação
# def criar_paginacao(request, objeto, tamanho_pagina=5):
#     paginator = Paginator(objeto, tamanho_pagina)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return page_obj


