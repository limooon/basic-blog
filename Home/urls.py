#
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '', 
        views.Homeview.as_view(),
        name='index',
    ),  
    path(
        'registrar-suscripcion', 
        views.SuscriberCreateView.as_view(),
        name='add-suscripcion',
    ),
    path(
        'contact', 
        views.ContactCreateView.as_view(),
        name='contact',
    ),
]