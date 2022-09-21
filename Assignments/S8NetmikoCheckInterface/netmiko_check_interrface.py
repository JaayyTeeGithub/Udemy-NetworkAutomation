from netmiko import ConnectHandler


ip = input('Enter IP of the device: ')
interface = input('Enter interface: ')

cisco_device = {
    'device_type': 'cisco_ios',
    'host': ip,
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
    }

connection = ConnectHandler(**cisco_device)
print('Enter enable mode')
connection.enable()

output = connection.send_command('show ip interface ' + interface)
if 'invalid input' in output:
    print('The interface entered is invalid!')
else:
    if ip not in output:
        print(interface + ' is down! Enabling the interface!')
        commands = ['interface ' + interface, 'no shut', 'exit']
        output = cisco_device.send_config_set(commands)
        print(output)
        print('#' * 30)
        print('The interface has been enabled!')
    else:
        print(interface + ' is up!')

print('Closing connection...')
connection.disconnect()
