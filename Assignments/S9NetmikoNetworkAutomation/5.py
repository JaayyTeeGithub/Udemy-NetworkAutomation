'''
Change the solution from the previous challenge so that the script saves the output of each command into its own file.
The name of the file should contain the router’s hostname.
'''
from netmiko import ConnectHandler
from datetime import datetime

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


now = datetime.now()
year = now.year
month = now.month
day = now.day

output = connection.send_command('show ip interface brief')
filename = f'{hostname}_{year}-{month}-{day}_showipintbrief.txt'
with open(filename, 'w') as f:
    f.write(output)

print('Entering enable mode...')
connection.enable()
filename = f'{hostname}_{year}-{month}-{day}_showrun.txt'
output = connection.send_command('show run')
print(output)
with open(filename, 'w') as f:
    f.write(output)
print('Closing connection...')
connection.disconnect()