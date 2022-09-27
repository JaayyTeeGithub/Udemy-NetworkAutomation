from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco'}  # enable password
ios = driver('10.1.1.10', 'username', 'password', optional_args=optional_args)
ios.open()  # start code

output = ios.get_facts()
# displays fully qualified domain name, hostname, interface list, model, os version, serial number, uptime, and vendor
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_arp_table()
# displays arp table
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_interfaces()
# returns info about interfaces. description, enabled state, up state, last flapped, mac address, and speed
dump = json.dump(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_interfaces_counters()
# displays metrics of interfaces. packets, discards, errors
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_interfaces_ip()
# displays ip of interfaces
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_bgp_neighbors()
# displays bgp neighbors. see if neighbors are up
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

output = ios.get_users()
# displays users on a device
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)

ios.close()  # end code
