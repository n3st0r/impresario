from jinja2 import Environment
from voiper.services.c7940 import template_c7940


def generate_config_c7940():
    cfg = Environment().from_string(template_c7940).render(
        sip_proxy='1.1.1.1',
        number1='123456789',
        secret1='abcdef',
        phone_label='Provider',
        secret='secret',
        phone_prompt='c7940_cmd',
        logo_url='http://ip/logo/ads.bmp',
        messages_uri='ADS'
    )

    return cfg
