'''
Create a Python script that connects to a Cisco Router using SSH and Netmiko. The script should create a user and then
save the running configuration of the router.

To create a user execute: username admin secret topsecret command in the global configuration mode.
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
print('Entering global configuration mode...')
connection.config_mode()
connection.send_command('username admin secret topsecret')
connection.exit_config_mode()
print('Saving configuration...')
connection.send_command('write')

print('Closing connection...')
connection.disconnect()

