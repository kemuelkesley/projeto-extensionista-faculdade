from .models import Condominio
from django.db.models import Q



def buscar_titulo_numero_condominio(search_value):
    if search_value:
        return Condominio.objects.filter(activate=True).filter(
            Q(condominium_number__icontains=search_value) | 
            Q(title__icontains=search_value)
        )
    else:
        return Condominio.objects.filter(activate=True)
    


def buscar_nome_titulo(search_value):
    if search_value:
        return Condominio.objects.filter(activate=True).filter(
            Q(condominium_name__icontains=search_value) | 
            Q(title__icontains=search_value)
        )
    else:
        return Condominio.objects.filter(activate=True)