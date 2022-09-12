import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


linux = {'hostname': '192.168.1.41', 'port': '22', 'username':'student', 'password': 'student'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('cat /etc/passwd\n')
time.sleep(1)

shell.send('sudo cat /etc/shadow\n')
shell.send('student\n')
time.sleep(1)


output = shell.recv(10000)
# print(type(output))
output = output.decode('utf-8')
print(output)


if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()

