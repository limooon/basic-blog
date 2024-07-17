from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings
from Entradas.models import Entry
from .managers import Manager
# Create your models here.


class Favorites(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    entry = models.ForeignKey(
        Entry,
        on_delete=models.CASCADE,
    )
    
    objects = Manager()

    class Meta:
        unique_together = ('user', 'entry')
        verbose_name = 'Entrada favorita'
        verbose_name_plural = 'Entradas favoritas'
        
    def __str__(self):
        return self.entry.title
