import csv

with open('devices.txt', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=':', lineterminator='')
    row_list = []
    for row in reader:
        row_list.append(row)

print(row_list)
