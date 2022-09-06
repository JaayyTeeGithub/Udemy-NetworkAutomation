'''
Consider the following Python list:

people = [

['Dan', 34, 'Bucharest'],

['Andrei',21, 'London'],

['Maria', 45, 'Paris']

]

Using the CSV module write each element of the list (which is another list) into a CSV file called people1.csv

After writing into the file, read and print out the file contents.

Use the default , (comma) as the delimiter.
'''

import csv

people = [

['Dan', 34, 'Bucharest'],

['Andrei',21, 'London'],

['Maria', 45, 'Paris']

]

with open('people.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for item in people:
        writer.writerow(item)

with open('people.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)