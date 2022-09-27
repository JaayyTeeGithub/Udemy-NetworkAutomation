import telnetlib
import time
'''
A Network Engineer has created this Python script that executes show ip interface brief on a remote Cisco Router using 
Telnet and displays the output.

However the script it’s hanging (nothing happens when it’s run).

Your task is to troubleshoot the issue and solve it so that it displays the output of the command.
'''
# connecting to the remote device (telnet server)
tn = telnetlib.Telnet('10.1.1.10')

tn.read_until(b'Username: ')
tn.write(b'u1\n')  # sending the username

tn.read_until(b'Password: ')
tn.write(b'cisco\n')  # sending the user's password


tn.write('terminal length 0\n'.encode())  # here it is
tn.write(b'show ip int brief\n')
tn.write(b'exit\n')
time.sleep(1)

# getting and printing the output
output = tn.read_all()
output = output.decode()
print(output)