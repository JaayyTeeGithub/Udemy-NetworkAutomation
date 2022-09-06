'''
Create a Python function called tail that reads the last n lines of a text file. The function has two arguments:
the file name and n (the number of lines to read). This is similar to the Linux `tail` command.

Example: tail('sample_file.txt', 5) will return the last 5 lines from sample_file.txt.
'''


def tail(filename, n):
    with open(filename, 'r') as file:
        content = file.read().splitlines()
        last = content[len(content)-n:]
        my_string = '\n'.join(last)
    return my_string


print(tail('sample_file.txt', 13))

