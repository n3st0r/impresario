from jinja2 import Environment
from django.core.exceptions import ObjectDoesNotExist
from voiper.models.number import Number


def create_sip_account(number):
    # try:
    #     number = Number.objects.get(pk=pk)
    #     # number = Number.objects.get(pk=pk).select_related('id_context')
    # except ObjectDoesNotExist:
    #     return False

    cfg = Environment().from_string(number.aster_template).render(
        number=number.number,
        secret=number.secret,
        context=number.id_context.name,
    ) + '\n\n'

    return cfg


def create_sip_accounts(numbers):
    config = ''
    for number in numbers:
        config += create_sip_account(number)

    return config
