import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname': '192.168.0.50', 'port': '22', 'username':'u1', 'password': 'pass123'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('sudo useradd u2\n', get_pty=True)
# when executing a command as root have to pass second argument to the exec_command method
# that argument is get_pty = True

stdin.write('pass123\n')  # this is the sudo password
time.sleep(2)  # waiting for the remote server to finish

stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n') # second command to show users
print(stdout.read().decode()) # reads byte data and converts to string before printing
time.sleep(1)


if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()