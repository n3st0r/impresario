from jinja2 import Environment
from voiper.services.c7940 import template_c7940


def generate_config_c7940(contracts, customer):
    data = {}
    for contract in contracts:
        line = str(contract.device_line)
        data['number_' + line] = contract.id_number.number
        data['secret_' + line] = contract.id_number.secret

    if 'number_2' not in data:
        data['number_2'] = ''
        data['secret_2'] = ''

    cfg = Environment().from_string(template_c7940).render(
        sip_proxy=customer.sip_proxy,
        logo_url=customer.logo_url,
        number1=data['number_1'],
        secret1=data['secret_1'],
        number2=data['number_2'],
        secret2=data['secret_2'],
        phone_label='Provider',
        secret='secret',
        phone_prompt='c7940_cmd',
        messages_uri=''
    )

    return cfg
