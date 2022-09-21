'''
Change the solution from the previous challenge so that the function receives a list of global configuration commands as
 its second argument and executes those commands on the device using Netmiko.

Example:

cmd = ['no router rip', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']

execute(cisco_device, cmd)
'''

from netmiko import ConnectHandler


def execute(device, command):
    connection = ConnectHandler(**device)
    output = connection.send_config_set(command)
    print(output)
    connection.disconnect()


cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
}
cmd = ['no router rip', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']
execute(cisco_device, cmd)

