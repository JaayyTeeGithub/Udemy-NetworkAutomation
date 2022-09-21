'''
Change the solution from the previous challenge so that the Python script reads the IP address of the device, the port,
the username, and the password from a file.

The file contains the login information on a single line in the format: IP:PORT:USERNAME:PASSWORD:ENABLE_PASSWORD

Example: 10.1.1.10:22:u1:cisco:cisco
'''

from netmiko import ConnectHandler
with open('2.txt', 'r') as f:
    devices = f.read().splitlines()

device_list = list()
for device in devices:
    output = device.split(':')
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': output[0],
        'username': output[2],
        'password': output[3],
        'port': output[1],
        'secret': output[4],
        'verbose': True
        }
    device_list.append(cisco_device)

for device in device_list:
    connection = ConnectHandler(**device)
    output = connection.send_command('show arp')
    print(output)
    print('Closing connection...')
    connection.disconnect()


