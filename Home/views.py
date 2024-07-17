
import datetime
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)

#app entrada
from Entradas.models import Entry 
from .models import Home
from .forms import SuscribersForm, ContactForm

class Homeview(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(Homeview,self).get_context_data(**kwargs)
        #texto de portada
        context["portada_home"] = Home.objects.latest('created')
        #cargamos el home
        context["portada"] = Entry.objects.entrada_en_portada()
        #contexto para los articulos en home
        context["entradas_home"] = Entry.objects.entrada_en_home()
        #contexto para entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        #envio de formulario de suscripcion
        context["form"] = SuscribersForm
        return context
    
    
class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url = '.'


class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url = '.'