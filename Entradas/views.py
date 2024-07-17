from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView
)

from .models import Entry, Category

class EntryListView(ListView):
    context_object_name = "entradas"
    paginate_by = 10
    template_name = "entradas/list.html"
    
    def get_context_data(self, **kwargs):
        context = super(EntryListView,self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all()
        return context
    
    
    def get_queryset(self):
        kword = self.request.GET.get("kword",'')
        categoria = self.request.GET.get("categoria",'')
        #consulta de busquedas
        resultado = Entry.objects.buscar_entrada(kword,categoria)
        return resultado
    
    
class EntryDetail(DetailView):
    model = Entry
    template_name='entradas/detail.html'