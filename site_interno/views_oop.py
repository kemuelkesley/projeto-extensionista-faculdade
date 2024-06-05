from django.core.paginator import Paginator
from django.shortcuts import render


class PaginatedListView:
    model = None
    template_name = None
    items_per_page = 5

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        paginator = Paginator(self.get_queryset(), self.items_per_page)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}
        context.update(kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


class IndexView(PaginatedListView):
    model = Condominio
    template_name = 'index.html'
    items_per_page = 5


class OperacionalView(PaginatedListView):
    model = Operacional
    template_name = 'operacional.html'
    items_per_page = 4


class TecnicoView(PaginatedListView):
    model = Tecnico
    template_name = 'tecnico.html'
    items_per_page = 5


class CondominioView(PaginatedListView):
    model = Condominio
    template_name = 'condominio.html'
    items_per_page = 10


def sobre(request):
    sobre = Sobre.objects.all()
    context = {'sobre': sobre}
    return render(request, 'sobre.html', context)
