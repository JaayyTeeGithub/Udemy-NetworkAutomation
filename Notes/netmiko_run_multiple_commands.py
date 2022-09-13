from netmiko import ConnectHandler
# connection object
cisco_device = {
       'device_type': 'cisco_ios',
       'host': '10.1.1.10',
       'username': 'u1',
       'password': 'cisco',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }

connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()

# this method receives a list of commands to send to the device
# in enters automatically into global config mode and exists automatically at the end
# netmiko has a method to enter multiple commands instead of using a for loop like with paramiko
commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']
# commands needed to create a loopback interface then create a user
output = connection.send_config_set(commands)
print(output)

## VARIATIONS
## 1.
cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'
connection.send_config_set(cmd.split(';'))
# allows you to use a string to input commands instead of using a list
# split by ';' delimiter

## 2.
# uses a multi string line instead of a string or list
cmd = '''ip ssh version 2
access-list 1 permit any
ip domain-name net-auto.io
'''
connection.send_config_set(cmd.split('\n'))
# split by '\n' delimiter


# in enters automatically into global config mode and exists automatically at the end
print(connection.find_prompt())

connection.send_command('write memory')
# command to save the configuration

print('Closing connection')
connection.disconnect()