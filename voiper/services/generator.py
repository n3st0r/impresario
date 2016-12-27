from jinja2 import Environment
from voiper.services.c7940 import template_c7940


def save_config(filename, contracts, customer):
#     if model.upper() == 'C7940':
#       generator = 'generate_config_c7940'
    print(filename)
    with open(filename, 'w') as file:
        config=generate_config_c7940(contracts, customer)
        file.write(config)


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
