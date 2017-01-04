from django.db import models
from django.core.urlresolvers import reverse


class Stencil(models.Model):

    name = models.CharField('Nazwa szablonu', max_length=21)
    description = models.CharField(
        'Opis',
        max_length=256
    )
    content = models.TextField(
        'Szablon konfiguracji',
        max_length=1024,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = "szablon konfiguracji"
        verbose_name_plural = "Szablon konfiguracji"

    def __str__(self):
        return self.name
