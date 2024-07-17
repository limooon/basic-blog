from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path(
        'entradas/', 
        views.EntryListView.as_view(),
        name='entradas-lista',
    ),  
    path(
        'entrada/<pk>/', 
        views.EntryDetail.as_view(),
        name='entrada-detail',
    ),  
     
]