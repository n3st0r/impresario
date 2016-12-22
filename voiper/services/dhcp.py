from voiper.models.devices import Device
from netaddr import EUI, mac_unix_expanded


def write_file(filename):
    with open(filename, 'w') as file:
        file.write(generate_config())


def get_devices():
    devices = Device.objects.all()

    return devices


def get_eui_mac(mac):
    eui = EUI(mac)
    eui.dialect = mac_unix_expanded
    return str(eui)


def host_definition(mac, model, ip):
    # host host9 {hardware ethernet mac; fixed-address ip; }
    eui = EUI(mac)
    eui.dialect = mac_unix_expanded
    ether = 'hardware ethernet %s' % get_eui_mac(mac)
    ipaddr = 'fixed-address %s' % ip
    config_line = 'host %s-%s {%s; %s;}\n' % (
        model,
        mac,
        ether,
        ipaddr,
    )
    return config_line


def generate_config():
    cnt = ''
    # devices = Device.objects.all()
    for device in get_devices():
        mac = device.mac
        model = device.dev
        ip = device.ip
        cnt += host_definition(mac=mac, model=model, ip=ip)

    return cnt
