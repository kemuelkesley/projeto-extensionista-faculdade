from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Operacional, Categoria, Tecnico, Condominio ,Sobre


def index(request):
    condominios = Condominio.objects.all()
    paginator = Paginator(condominios, 5) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    
    return render(request, "index.html", {"page_obj": page_obj, "condominios": condominios})



def operacional(request):
    operacional = Operacional.objects.all()
    paginator = Paginator(operacional, 4)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request, 'operacional.html', {"page_obj": page_obj, "operacional": operacional})


def tecnico(request):
    tecnico = Tecnico.objects.all()
    categorias = Categoria.objects.all()

    paginator = Paginator(categorias, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    return render(request, 'tecnico.html', {"page_obj": page_obj, "tecnico": tecnico, "categorias": categorias})


def condominio(request):
    condominios = Condominio.objects.all()
    paginator = Paginator(condominios, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

   
    return render(request, 'condominio.html', {"page_obj": page_obj, "condominios": condominios})


def sobre(request):
    sobre = Sobre.objects.all()
    
    context = {
        'sobre': sobre
    }
    return render(request, 'sobre.html', context)


