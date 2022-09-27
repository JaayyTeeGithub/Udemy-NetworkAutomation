import telnetlib
import time
'''
Create a Python script that connects to a Cisco Router using Telnet and executes the show users command in order to 
display the logged-in users.

Print out the output of the command.
'''

# connecting to the remote device (telnet server)
tn = telnetlib.Telnet('10.1.1.10')

tn.read_until(b'Username: ')
tn.write(b'u1\n')  # sending the username

tn.read_until(b'Password: ')
tn.write(b'cisco\n')  # sending the user's password

tn.write(b'show users\n')
tn.write(b'exit\n')
time.sleep(1)

# getting and printing the output
output = tn.read_all()
output = output.decode()
print(output)