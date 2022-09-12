import myparamiko
import getpass

username = input('Enter username: ')
password = getpass.getpass()


client = myparamiko.connect('192.168.1.41', '22', username, password)
shell = myparamiko.get_shell(client)
new_username = input('Enter new username: ')
command = 'sudo useradd -m -d /home/' + new_username + ' -s /bin/bash ' + new_username
myparamiko.send_command(shell, command)
myparamiko.send_command(shell, password)
print('User has been created!')

user_input = input('Display users? <y/n>')
if user_input.lower() == 'y':
    users = myparamiko.send_command(shell,'cat /etc/passwd')
    print(users.decode())

myparamiko.close(client)
