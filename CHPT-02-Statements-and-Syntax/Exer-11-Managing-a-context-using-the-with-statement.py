# Exer-11-Managing-a-context-using-the-with-statement

import csv
import pathlib

some_source = [[2,3,5], [7,11,13], [17,19,23]]
target_path = pathlib.Path('code/test.csv')
with target_path.open('w', newline='') as target_file:
    writer = csv.writer(target_file)
    writer.writerow(['column', 'data', 'headings'])
    for data in some_source:
        writer.writerow(data)

print('finished writing', target_path)

###

try:
    target_path = pathlib.Path('code/test.csv')
    with target_path.open('w', newline='') as target_file:
        writer = csv.writer(target_file)
        writer.writerow(['column', 'headings'])
        for data in some_source:
            writer.writerow(data)
            raise Exception("Just Testing")
except Exception as exc:
    print(target_file.closed)
    print(exc)
print('finished writing', target_path)
