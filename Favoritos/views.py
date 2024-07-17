from django.shortcuts import render
from .models import Favorites
from django.views.generic import ListView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from Entradas.models import Entry
from django.views import View


class UserNameList(LoginRequiredMixin,ListView):
    model = Favorites
    context_object_name = 'entradas_user'
    template_name='favoritos/perfil.html'
    login_url=reverse_lazy('users_app:user-login')
    
    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)
    
#agraga favoritos
class AddFavoritosViwe(LoginRequiredMixin,View):
    login_url=reverse_lazy('users_app:user-login')
     
    def post(self, request, *args, **kwargs):
        #recuperar un usuario
        usuario = self.request.user
        #recuperamos el id dela entrada desde la url
        entrada = Entry.objects.get(id=self.kwargs['pk'])
        #registramos favoritos
        Favorites.objects.create(
            user=usuario,
            entry=entrada,
        )
        
        return HttpResponseRedirect(
            reverse(
                'favoritos_app:perfil',
            )
        )

class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favoritos_app:perfil')
    
