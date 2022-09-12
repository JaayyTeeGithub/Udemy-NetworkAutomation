import myparamiko # myparamiko.py should be in the same directory with this script (or in sys.path)
import threading

def backup(router):
    client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(client)

    myparamiko.send_command(shell, 'terminal length 0')
    myparamiko.send_command(shell, 'enable')
    myparamiko.send_command(shell, 'cisco')  # this is the enable command
    myparamiko.send_command(shell, 'show run')

    output = myparamiko.show(shell)

    # processing the output
    # print(output)
    output_list = output.splitlines()
    output_list = output_list[11:-1]
    # print(output_list)
    output = '\n'.join(output_list)
    # print(output)

    # creating the backup filename
    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    file_name = f'{router["server_ip"]}_{year}-{month}-{day}.txt'
    print(file_name)

    # writing the backup to the file
    with open(file_name, 'w') as f:
        f.write(output)

    myparamiko.close(client)


# creating a dictionary for each device to connect to
router1 = {'server_ip':'10.1.1.10', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
router2 = {'server_ip':'10.1.1.20', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
router3 = {'server_ip':'10.1.1.30', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}

# creating a list of dictionaries (of devices)
routers = [router1, router2, router3]

threads = list()

for router in routers:
    # iterate over routers and create a thread for each one
    th = threading.Thread(target=backup, args=(router,))
    # add the routers to a list
    threads.append(th)

for th in threads:
    # iterate over threads and start them
    th.start()

for th in threads:
    # wait for each thread to finish and then close
    th.join()

