from django.db import models
from voiper.models import Device
from voiper.models import Number


class Contract(models.Model):
    LINE_NUMBER = (
            (1, 'Linia pierwsza'),
            (2, 'Linia druga'),
    )
    id_device = models.ForeignKey(Device, verbose_name="Urządzenie VoIP")
    id_number = models.OneToOneField(Number, verbose_name="Numer telefonu")
    device_line = models.IntegerField('Linia urządzenia', choices=LINE_NUMBER)

    class Meta:
        unique_together = ("id_device", "device_line")
        ordering = ('id_device', 'device_line')

    def __str__(self):
        return "%s, LINIA::%s, Urządzenie:: %s" % (self.id_number, self.device_line, self.id_device)
