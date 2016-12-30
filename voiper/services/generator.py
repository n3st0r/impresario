from jinja2 import Environment
from voiper.services.c7940 import template_c7940
from voiper.services.pap2t import template_pap2


def generate_config(contracts, customer, model, filename, save=False):
    print('test1' + str(model).upper())
    if str(model).upper() == 'C7940':
        print('test2')
        generator = eval('generate_config_c7940')
        # filename = 'SIP' + mac.upper() + '.cnf'
    elif str(model).upper() == 'PAP2-NA':
        print('test - PAP2T-NA')
        generator = eval('generate_config_pap2t')
    # if generator:
    config = generator(contracts, customer)

    if save:
        save_config(filename, config)
    else:
        return config


def save_config(filename, config):

    # print(filename)
    with open(filename, 'w') as file:
        # config = generator(contracts, customer)
        file.write(config)
        return True


def generate_config_c7940(contracts, customer):
    print('Test Generator')
    data = {}
    for contract in contracts:
        line = str(contract.device_line)
        data['number_' + line] = contract.id_number.number
        data['secret_' + line] = contract.id_number.secret

    if 'number_2' not in data:
        data['number_2'] = ''
        data['secret_2'] = ''

    cfg = Environment().from_string(template_c7940).render(
        data,
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


def generate_config_pap2t(contracts, customer):
    data = {}
    for contract in contracts:
        line = str(contract.device_line)
        data['number_' + line] = contract.id_number.number
        data['secret_' + line] = contract.id_number.secret

    if 'number_2' not in data:
        data['number_2'] = ''
        data['secret_2'] = ''

    config = Environment().from_string(template_pap2).render(
        data,
        sip_proxy=customer.sip_proxy,
        provisioning_rule='tftp://192.168.99.2/voip/pap2t-na/$MA.cfg',
    )
    return config
