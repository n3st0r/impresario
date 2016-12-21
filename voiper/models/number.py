from django.db import models
from impresario.models import Customer
from voiper.models import Context
import random


class Number(models.Model):
    def gen_password():
        size=21
        tablica='abcdefghjkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789'
        return ''.join(random.choice(tablica) for _ in range(size))

    number = models.CharField(max_length=9)
    secret = models.CharField(max_length=32, default=gen_password())
    id_customer = models.ForeignKey(Customer, verbose_name="Klient")
    id_context = models.ForeignKey(Context, verbose_name="Kontekst")

    class Meta:
        ordering = ('number', )

    def __str__(self):
        return self.number
