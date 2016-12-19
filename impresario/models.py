from django.db import models
from django.core.urlresolvers import reverse


class Person(models.Model):
    """
    Person model.
    """
    first_name = models.CharField('Imię', max_length=32)
    last_name = models.CharField('Nazwisko', max_length=32)

    class Meta:
        app_label = "impresario"
        verbose_name = 'osoba'
        verbose_name_plural = 'osoby'

    def get_absolute_url(self):
        return reverse("impresario:persons_list", kwargs={'pk': self.pk})
