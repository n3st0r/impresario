from voiper.models.devices import Device


def write_file(filename):
    devices = get_devices()
    with open(filename, 'w') as file:
        for device in devices:
            line = host_definition(device)
            file.write(line)


def get_devices():
    devices = Device.object.all()

    return devices


def host_definition(host):
    mac = host.mac
    line = 'host %s' % (mac)
    return line
