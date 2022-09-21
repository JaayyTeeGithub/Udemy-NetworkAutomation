'''
Create a Python script that connects to a Cisco Router using SSH and Netmiko. The script should get the prompt,
process it and then print the hostname part.
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
prompt = connection.find_prompt()
hostname = prompt[:-1]
print('Disconnecting from ' + hostname)
connection.disconnect()