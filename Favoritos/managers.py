from django.db import models

class Manager(models.Manager):
    def entradas_user(self,usuario):
        return self.filter(
            entry__public=True,
            user=usuario
        ).order_by('-created')

