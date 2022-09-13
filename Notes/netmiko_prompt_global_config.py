from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
       'host': '10.1.1.10',
       'username': 'u1',
       'password': 'cisco',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }
connection = ConnectHandler(**cisco_device)

# getting the router's prompt to see what mode we are currently in
prompt = connection.find_prompt()
if '>' in prompt:
       connection.enable()   # entering the enable mode

output = connection.send_command('sh run')
print(output)

# print(connection.check_config_mode())
# will print false because we are not in the global configuration mode

if not connection.check_config_mode(): # returns True if it's already in the global config mode
       connection.config_mode()  # entering the global config mode

# print(connection.check_config_mode())
# will print true because we are in the global configuration mode

connection.send_command('username u3 secret cisco') #command to create a user

# command to check users is 'sh run | include user'

connection.exit_config_mode()  # exiting the global config mode
print(connection.check_config_mode()) # checks to see if in global configuration mode, returns false

print('Closing connection')
connection.disconnect()