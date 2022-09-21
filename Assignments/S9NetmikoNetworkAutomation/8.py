'''
Create a Python script that connects to a Cisco Router using SSH and Netmiko. The script should create an ACL
(access control list) by executing the following 3 commands:

access-list 101 permit tcp any any eq 80

access-list 101 permit tcp any any eq 443

access-list 101 deny ip any any

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

commands = ['access-list 101 permit tcp any any eq 80', 'access-list 101 permit tcp any any eq 443',
            'access-list 101 deny ip any any']

print('Sending commands to device...')
connection.send_config_set(commands)

print('Closing connection...')
connection.disconnect()