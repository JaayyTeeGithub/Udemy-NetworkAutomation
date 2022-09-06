'''
Create a Python script that reads a text file into a list and then converts the list back into a string which is the
 entire file content.
'''

with open('sample_file.txt') as file:
    file_list = file.readlines()
    print(file_list)
    print(''.join(file_list))
    