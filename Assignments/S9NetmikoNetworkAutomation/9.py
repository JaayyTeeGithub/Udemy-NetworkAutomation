'''
Change the solution from the previous challenge so that the script will also display the commands that were executed.
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
output = connection.send_config_set(commands)
print(output)

print('Closing connection...')
connection.disconnect()