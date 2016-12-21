from django.db import models


class Context(models.Model):
    name = models.CharField('Nazwa kontekstu', max_length=16)
    description = models.TextField('Opis przeznaczenia kontekstu')

    def __str__(self):
        return self.name
