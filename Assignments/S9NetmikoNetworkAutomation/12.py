'''
Change the solution from the previous challenge so that the script will save the output to a file instead of
printing it out.

Each filename should contain the hostname and current date.
'''
from netmiko import ConnectHandler
from datetime import datetime

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
    prompt = connection.find_prompt()
    hostname = prompt[:-1]
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    filename = f'{hostname}_{year}-{month}-{day}.txt'
    with open(filename, 'w') as f:
        f.write(output)

    print(output)

    connection.disconnect()
    print('#' * 30)