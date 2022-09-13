from netmiko import ConnectHandler

linux = {
    'device_type': 'linux',
    'host': '192.168.1.41',
    'username': 'student',
    'password': 'student',
    'port': 22,
    'secret': 'student',  # sudo password
    'verbose': True
    }

connection = ConnectHandler(**linux)

connection.enable()  # same as sudo su
#  install apache2
output = connection.send_command('apt update && apt install -y apache2')


print('closing connection')
connection.disconnect()


