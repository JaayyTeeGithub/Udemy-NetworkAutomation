'''
Create a Python script that connects to each Router using Netmiko, execute show ip interface brief and display the output.

The IP addresses of the routers are saved in a Python list.
'''

from netmiko import ConnectHandler

devices = ['10.1.1.10', '192.168.122.20', '192.168.122.30']
for device in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': device,
        'username': 'u1',
        'password': 'cisco',
        'port': 22,
        'secret': 'cisco',
        'verbose': True
        }
    connection = ConnectHandler(**cisco_device)
    output = connection.send_command('show ip int brief')
    print(output)

    connection.disconnect()
    print('#' * 30)