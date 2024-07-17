from django.db import models
from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):
    title = models.CharField('nombre',max_length=50)
    descripcion = models.TextField()
    about_title = models.CharField('titulo nosotros',max_length=50)
    phone = models.CharField('telefono contacto',max_length=10)
    
    class Meta:
        
        verbose_name = 'Pagina principal'
        verbose_name_plural = 'Pagina principal'
        
    def __str__(self):
        return self.title
    

class Suscriber(TimeStampedModel):
    email = models.EmailField('Email',max_length=254)
    
    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscripciones'
        
    def __str__(self):
        return self.email
    

class Contact(TimeStampedModel):
    full_name = models.CharField('nombres',max_length=50)
    email = models.EmailField('email', max_length=254)
    message = models.TextField()
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        return self.full_name