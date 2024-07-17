from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField


# maqnagers
from .managers import EntryManager

class Category(TimeStampedModel):
    short_name = models.CharField('nombre corto', max_length=50,unique=True)
    name = models.CharField('nombre', max_length=50)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.name

  
class Tag(TimeStampedModel):
    "etiqueta de un articulo"
    name = models.CharField('nombre', max_length=50)
    
    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'
        
    def __str__(self):
        return self.name
    
class Entry(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField('titulo', max_length=50)
    resume = models.TextField('resumen')
    content = RichTextUploadingField('contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField('imagen', upload_to='media')
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    

    
    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        
    def __str__(self):
        return self.title
    
    