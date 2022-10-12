# Exer-04-Deleting-from-a-list-deleting-removing-popping-and-filtering

from pathlib import Path
import csv

with Path('fuel.csv').open() as source_file:
    reader = csv.reader(source_file)
    log_rows = list(reader)
print(log_rows[0])
print(log_rows[-1])

tail = log_rows.copy()

del tail[:4]
print(tail[0])

###

row = ['10/25/13', '08:24:00 AM', '29', '', '01:15:00 PM', '27']
row.remove("")
print(row)

###

row = ['10/25/13', '08:24:00 AM', '29', '', '01:15:00 PM', '27']
target_position = row.index('')
print(target_position)
row.pop(target_position)
print(row)

###

def number_column(row, column=2):
    try:
        float(row[column])
        return True
    except ValueError:
        return False

tail_rows = list(filter(number_column, log_rows))
print(len(tail_rows))
print(tail_rows[0])
print(tail_rows[-1])

row = ['', '06:25:00 PM', '22']
del row[3] # IndexError

###

data_items = [1, 1, 2, 3, 5, 8, 10, 13, 21, 34, 36, 55]
for f in data_items:
    if f%2 == 0:
        data_items.remove(f)  # The 10 will never be processed.

print(data_items)

###
data_items = [1, 1, 2, 3, 5, 8, 10, 13, 21, 34, 36, 55]
position = 0
while position != len(data_items):
    f = data_items[position]
    if f%2 == 0:
        data_items.remove(f)
    else:
        position += 1
print(data_items)

