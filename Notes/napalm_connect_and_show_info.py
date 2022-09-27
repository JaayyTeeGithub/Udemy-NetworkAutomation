from napalm import get_network_driver
import json

driver = get_network_driver('ios')  # documentation includes additional devices
optional_args = {'secret': 'cisco'}  # cisco is the enable password
ios = driver('10.1.1.10', 'username', 'password', optional_args=optional_args)

ios.open()  # start of code

print(dir(ios))

output = ios.get_arp_table()
for item in output:
    print(item)

dump = json.dumps(output, sort_keys=True, indent=4)
#  sorted and indented in json for readability
print(dump)

#  write dump to file
with open('arp.txt', 'w') as f:
    f.write(dump)

ios.close()  # end of code
