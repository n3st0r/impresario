from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings


class Device(models.Model):
    DEVICE_MODEL = (
        ('PAP2-NA', 'Bramka PAP2-NA'),
        ('SPA2102', 'Bramka SPA2102'),
        ('C7940', 'Telefon C7940'),
        ('CP-8851', 'Telefon CP-8851')
    )

    mac = models.CharField('Adres MAC urządzenia', max_length=12)
    ip = models.GenericIPAddressField('Adres IP urządzenia', protocol='ipv4')
    dev = models.CharField('Model urządzenia', max_length=8, choices=DEVICE_MODEL)

    def __str__(self):
        return "MAC: %s, Model %s, IP: %s" % (self.mac.upper(), self.dev, self.ip)

    def get_absolute_url(self):
        return reverse("voiper:voip_device_edit", kwargs={'pk': self.pk})

    @property
    def config_filename(self):
        if self.dev == 'C7940':
            return 'SIP' + self.mac.upper() + '.cnf'
        elif self.dev == 'PAP2-NA':
            return self.mac.lower() + '.cfg'

    def get_option(self):
        data = settings.VOIPER
        data['model'] = self.dev
        data['mac'] = self.mac
        return data
