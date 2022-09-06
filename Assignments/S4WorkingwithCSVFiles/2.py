'''
Change the solution from the previous challenge and use : (colon) as the delimiter.
'''

import csv

people = [

['Dan', 34, 'Bucharest'],

['Andrei',21, 'London'],

['Maria', 45, 'Paris']

]

with open('people.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=':')
    for item in people:
        writer.writerow(item)

with open('people.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=':')
    for row in reader:
        print(row)