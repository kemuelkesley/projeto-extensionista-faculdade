from django.core.paginator import Paginator


def criar_paginacao(request, queryset, num_per_page):
    paginator = Paginator(queryset, num_per_page)
    page_number = request.GET.get('page')
    
    return paginator.get_page(page_number)
