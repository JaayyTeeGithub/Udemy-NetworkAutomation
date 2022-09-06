'''
Write a Python program that calculates the net amount of a bank account based on the transactions saved in a text file.

The file format is as following:

D:50

W:100

D means deposit while W means withdrawal.

Suppose that the following file is supplied to the program:

D:300

D:300

W:500

D:200

Then, the output should be: 300
'''


def net_amount(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        total = 0
        for line in lines:
            if line[0] == 'D':
                total += int(line[2:])
            else:
                total -= int(line[2:])
    return total


print(net_amount('banking.txt'))
