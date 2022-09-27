import telnetlib
import time
'''
Create a Python script that connects to a Cisco Router using Telnet and executes a list of commands. The commands are 
saved in a Python list.

An example of a list with commands to execute:

# the second element (cisco) is the enable command

commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end', 'terminal 
length 0', 'sh run | i user']
'''
commands = ['enable', 'cisco', 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end',
            'terminal length 0', 'sh run | i user']
host = '10.1.1.10'
user = 'u1'
password = 'cisco'

tn = telnetlib.Telnet(host)

tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

tn.write(b'terminal length 0\n')

for command in commands:
    tn.write(command.encode() + b'\n')

tn.write('exit\n'.encode())
time.sleep(2)

output = tn.read_all()
print(type(output))
output = output.decode()
print(output)