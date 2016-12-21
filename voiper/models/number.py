from django.db import models
from django.core.urlresolvers import reverse
from impresario.models import Customer
from voiper.models import Context
from voiper.services.security import gen_password


class Number(models.Model):

    number = models.CharField(max_length=9)
    secret = models.CharField(max_length=32, default=gen_password())
    id_customer = models.ForeignKey(Customer, verbose_name="Klient")
    id_context = models.ForeignKey(Context, verbose_name="Kontekst")

    class Meta:
        ordering = ('number', )

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("voip_numbers:edit", kwargs={'pk': self.pk})
