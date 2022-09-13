#!/usr/bin/env python3

import paramiko
import getpass
from datetime import datetime
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass('Enter password: ')
router = {'hostname': '192.168.122.100', 'port': '22', 'username': 'u1', 'password': password}

print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
time.sleep(1)
shell.send('enable\n')
time.sleep(1)
shell.send('cisco\n')
time.sleep(1)
shell.send('show run\n')
time.sleep(2)
output = shell.recv(10000).decode()
print(output)

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

file_name = f'{router["hostname"]}_{year}-{month}-{day}.txt'

with open(file_name, 'w') as f:
    f.write(output)

if ssh_client.get_transport().is_active():
    print('Closing connection...')
    ssh_client.close()
