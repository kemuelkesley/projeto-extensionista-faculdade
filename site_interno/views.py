from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Operacional, Categoria, Tecnico, Condominio ,Sobre
# Importando a função de busca no banco de dados
from .sql import buscar_titulo_numero_condominio, buscar_nome_titulo
# Importando a função de paginação
from .metodos_genericos import criar_paginacao



def index(request):
    search_value = request.GET.get('q', '').strip()
    
    # Use a função de busca para obter os resultados filtrados
    condominios = buscar_titulo_numero_condominio(search_value)
    
    
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

    search_value = request.GET.get('q', '').strip()

    condominios = buscar_nome_titulo(search_value)

    paginas = criar_paginacao(request, condominios, 10)
    page_obj = paginas

    context = {
        "page_obj": page_obj,
        "search_value": search_value,
        "no_results": not condominios.exists()
    }

   
    return render(request, 'condominio.html', context)


def sobre(request):
    sobre = Sobre.objects.filter(activate=True)
    
    context = {
        'sobre': sobre
    }
    return render(request, 'sobre.html', context)

