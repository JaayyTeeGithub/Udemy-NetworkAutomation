import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname': '192.168.1.41', 'port': '22', 'username':'student', 'password': 'student'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

# each Linux command runs in its own shell and has its own input, output and error
stdin, stdout, stderr = ssh_client.exec_command('ifconfig\n')
output = stdout.read() # reads the output of the command by calling the read method
output = output.decode() # type is bytes, so decode to get string
print(output)

# exec_commands must be called on each command
stdin, stdout, stderr = ssh_client.exec_command('cat /etc/shadow\n')
time.sleep(0.5) # pause is need to wait for command to run
output = stdout.read()
output = output.decode()
print(output)

# reading from standard error
print(stderr.read().decode())

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()