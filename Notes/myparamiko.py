import paramiko
import time


def connect(server_ip, server_port, user, passwd):
    '''
    creates a connection with a device
    :param server_ip:
    :param server_port:
    :param user:
    :param passwd:
    :return: instance of the client
    '''
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd,
                       look_for_keys=False, allow_agent=False)
    return ssh_client # have to return client or else it will be lost


def get_shell(ssh_client):
    '''
    :param ssh_client: client created by connect function
    :return: the shell object for the ssh_client
    '''

    shell = ssh_client.invoke_shell()
    return shell


def send_command(shell, command, timout=1):
    '''
    :param shell: shell object from get_shell function
    :param command: command to be passed to the device
    :param timout:
    :return: none
    '''
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timout)


def show(shell, n=10000):
    '''
    shows output of device
    :param shell: shell object from get_shell function
    :param n:
    :return: decode output from shell
    '''
    output = shell.recv(n)
    return output.decode()


def close(ssh_client):
    '''
    closes a connection with a device
    :param ssh_client: client from connect function
    :return: none
    '''
    if ssh_client.get_transport().is_active():
        print('Closing connection')
        ssh_client.close()


if __name__ == '__main__':
    router1 = {'server_ip': '10.1.1.10', 'server_port': '22', 'user':'u1', 'passwd':'cisco'}
    client = connect(**router1)
    shell = get_shell(client)

    send_command(shell, 'enable') # enters enable mode
    send_command(shell, 'cisco') # this is the enable password
    send_command(shell, 'term len 0') # show all output
    send_command(shell, 'sh version')
    send_command(shell, 'sh ip int brief')

    output = show(shell)
    print(output) # shows output from previous commands



