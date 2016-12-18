from django.db import models


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
