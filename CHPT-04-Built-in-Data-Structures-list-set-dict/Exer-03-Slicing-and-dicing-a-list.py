# Exer-03-Slicing-and-dicing-a-list

from pathlib import Path
import csv

with Path('fuel.csv').open() as source_file:
    reader = csv.reader(source_file)
    log_rows = list(reader)
#print(log_rows[0])
#print(log_rows[-1])

head, tail = log_rows[:4], log_rows[4:]
#print(head[0])
#print(head[-1])

#print(tail[0])
#print(tail[-1])

# every third row, starting with row zero
# print(tail[0::3])

# every third row, starting with row one
#print(tail[1::3])

# zip two slices together
#print(list( zip(tail[0::3], tail[1::3])  ))

paired_rows = list( zip(tail[0::3], tail[1::3])  )
print([a+b for a,b in paired_rows])

