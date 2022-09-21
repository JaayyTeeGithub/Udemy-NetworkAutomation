'''
Create a Python script that connects to a Cisco Router using SSH and Netmiko. The script should execute the show arp
command in order to display the ARP table.

Print out the output of the command.
'''

from netmiko import ConnectHandler

ip = '10.1.1.10'

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
output = connection.send_command('show arp')
print(output)

print('Closing connection...')
connection.disconnect()

