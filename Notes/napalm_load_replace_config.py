from napalm import get_network_driver

# napalm uses SCP for configuration management
# make sure SCP is good on the router
# archive needs to be ran on the router or else you will get an error

driver = get_network_driver('ios')
optional_args={'secret': 'cisco'}
ios = driver('10.1.1.10', 'username', 'password', optional_args=optional_args)
ios.open()

ios.load_replace_candidate(filename='config.txt')
diff = ios.compare_config()
# compares configurations and displays the differences between running configuration and the configuration file
print(diff)
if len(diff):
    print('Commit changes...')
    ios.commit_config()
    # commits changes to router
    print('Done')
else:
    print('No changes required')
    ios.discard_config()

ios.close()