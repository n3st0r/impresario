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

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    def get_absolute_url(self):
        return reverse("impresario:persons_edit", kwargs={'pk': self.pk})


class Customer(models.Model):
    name = models.CharField(max_length=32)
    contact = models.ManyToManyField(Person)
    sip_proxy = models.GenericIPAddressField('SIP proxy', protocol='IPv4', null=True)
    logo_url = models.URLField('Adres URL logo', max_length=100, null=True)

    class Meta:
        app_label = "impresario"
        verbose_name = 'klient'
        verbose_name_plural = 'klienci'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass
        # return reverse("impresario:customer_edit", kwargs={'pk': self.pk})
