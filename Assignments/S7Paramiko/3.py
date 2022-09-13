'''

Change the solution from Challenge #1 so that it will save the output to a file instead of printing it.

'''

import paramiko
import getpass
import time


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

username = input('Enter username: ')
password = getpass.getpass('Enter password: ') # challenge 2 was to use getpass. I already did

host = {'hostname': '192.168.1.41', 'port': '22', 'username': username, 'password': password}
print(f'Connecting to {host["hostname"]}')
ssh_client.connect(**host, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
output = stdout.read().decode()
time.sleep(1)

with open('users.txt', 'w') as f:
    f.write(output)

if ssh_client.get_transport().is_active():
    print('CLosing Connection')
    ssh_client.close()