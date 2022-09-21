'''
Change the solution from the previous challenge so that the script will prompt for both the user that authenticates and
the enable passwords securely (use getpass module). Run the script in the terminal (you can not run it in PyCharm).
'''

from netmiko import ConnectHandler
from datetime import datetime
import getpass

username = input('Enter username: ')
password = getpass.getpass('Enter password: ')
enable_password = getpass.getpass('Enter enable password: ')

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.1.1.10',
    'username': username,
    'password': password,
    'port': 22,
    'secret': enable_password,  # this is the enable password
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