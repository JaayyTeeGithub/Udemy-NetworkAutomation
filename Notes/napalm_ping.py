from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco'}
ios = driver('10.1.1.10', 'username', 'password', optional_args=optional_args)
ios.open()

output = ios.ping('10.1.1.20')
# displays probes sent, packet loss, round trip time stats
ping = json.dumps(output, sort_keys=True, indent=4)
print(ping)

output = ios.ping(destination='10.1.1.20', count=2, source='1.1.1.1')
# specifies destination and source. specifies packets
ping = json.dumps(output, sort_keys=True, indent=4)
print(ping)

ios.close()