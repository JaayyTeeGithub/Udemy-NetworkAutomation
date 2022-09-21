'''
Create a Python script that connects to a Cisco Router using SSH and Netmiko. The script should execute the show ip int
brief and show run commands.

Print out the output of each command.
'''
from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',  # this is the enable password
    'verbose': True
}

connection = ConnectHandler(**cisco_device)
output = connection.send_command('show ip interface brief')
print(output)
print('Entering enable mode...')
connection.enable()
output = connection.send_command('show run')
print(output)
print('Closing connection...')
connection.disconnect()