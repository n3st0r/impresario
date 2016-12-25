from django.db import models
from django.core.urlresolvers import reverse


class Context(models.Model):
    name = models.CharField('Nazwa kontekstu', max_length=16)
    description = models.TextField('Opis przeznaczenia kontekstu')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("voip_context:edit", kwargs={'pk': self.pk})
