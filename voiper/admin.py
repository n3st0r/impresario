from django.contrib import admin

from voiper.models import Device, Context, Number, Contract

admin.site.register(Device)
admin.site.register(Context)
admin.site.register(Contract)
admin.site.register(Number)
