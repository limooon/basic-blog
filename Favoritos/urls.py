from django.urls import path
from . import views

app_name = "favoritos_app"

urlpatterns = [
    path(
        'perfil/', 
        views.UserNameList.as_view(),
        name='perfil',
    ),  
    path(
        'add-entrada/<pk>', 
        views.AddFavoritosViwe.as_view(),
        name='add-favoritos',
    ), 
    path(
        'delete-favoritos/<pk>', 
        views.FavoritesDeleteView.as_view(),
        name='delete-favoritos',
    ), 
   
]