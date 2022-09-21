'''
Create a Python script that connects to a Cisco Router using SSH and Netmiko and executes all the commands
from 10.txt.

Note: Try to execute the commands by a single method call.
'''
from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
    }

connection = ConnectHandler(**cisco_device)

print('Entering enable mode...')
connection.enable()

output = connection.send_config_from_file('10.txt')
print(output)

print('Closing connection...')
connection.disconnect()