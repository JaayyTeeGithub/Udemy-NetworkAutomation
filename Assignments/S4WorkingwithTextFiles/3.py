'''
Change the solution from the previous challenge so that the script that prints out the last n lines of the file
refreshes the output every 3 seconds (as the file changes or updates). This is similar to `tail -f` Linux command
'''

import time


def tail(filename, n):
    with open(filename, 'r') as file:
        content = file.read().splitlines()
        last = content[len(content)-n:]
        my_string = '\n'.join(last)
    return my_string


while True:
    print(tail('sample_file.txt', 13) + '\n')
    time.sleep(3)