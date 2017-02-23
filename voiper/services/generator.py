from jinja2 import Environment
from voiper.services.c7940 import template_c7940
from voiper.services.pap2t import template_pap2


def generate_config(contracts, customer, option, save=False):
    data = prepare_data(contracts=contracts, option=option)
    data['sip_proxy'] = customer.sip_proxy
    data['dir'] = option['cfg_dir'] + option['model'].lower() + '/'
    if str(option['model']).upper() == 'C7940':
        generator = eval('generate_config_c7940')
        data['logo_url'] = customer.logo_url

        data['filename'] = 'SIP' + option['mac'].upper() + '.cnf'
        data['secret'] = 'secret'
        data['phone_prompt'] = 'c7940_cmd'
        data['messages_uri'] = ''

    elif str(option['model']).upper() == 'PAP2-NA':
        generator = eval('generate_config_pap2t')
        data['filename'] = option['mac'].lower() + '.cfg'
        data['provisioning_rule'] = 'tftp://%s/voip/pap2t/$MA.cfg' % option['tftp']
        data['upgrade_rule'] = '(&lt; 5.1.6)? tftp://%s/voip/pap2t-5-1-6.bin' % option['tftp']
        data['dir'] = option['cfg_dir'] + 'pap2t/'
    # if generator:
    config = generator(data)
    filename = data['dir'] + data['filename']
    print(filename)
    if save:
        filename = data['dir'] + data['filename']
        save_config(filename, config)
    else:
        return config


def prepare_data(contracts, option):
    data = {}
    for contract in contracts:
        line = str(contract.device_line)
        data['number_' + line] = contract.id_number.number
        data['secret_' + line] = contract.id_number.secret

    if 'provider' in option:
        data['provider'] = option['provider']

    return data


def save_config(filename, config):
    with open(filename, 'w') as file:
        file.write(config)


def generate_config_c7940(data):
    print('Test Generator')

    cfg = Environment().from_string(template_c7940).render(
        data=data,

    )
    return cfg


def generate_config_pap2t(data):
    data['dialplan_1'] = '(*xx|11x|4xxx|[1-9]xxxxxxxx|0[1-9]xxxxxxxx|00[1-9]xxxxxxx.|019xxx)'
    data['dialplan_2'] = '(*xx|11x|4xxx|[1-9]xxxxxxxx|0[1-9]xxxxxxxx|00[1-9]xxxxxxx.|019xxx)'

    config = Environment().from_string(template_pap2).render(data=data)
    return config
