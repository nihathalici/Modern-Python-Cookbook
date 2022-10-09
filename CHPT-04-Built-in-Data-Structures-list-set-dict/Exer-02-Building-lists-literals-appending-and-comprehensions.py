# Exer-02-Building-lists-literals-appending-and-comprehensions

import pathlib

home = pathlib.Path('source')
for path in home.glob('*/index.rst'):
    print(path.stat().st_size, path.parent)

###

file_sizes = []
home = pathlib.Path('source')
for path in home.glob('*/index.rst'):
    file_sizes.append(path.stat().st_size)
print(file_sizes)
print(sum(file_sizes))

###

[path.stat().st_size for path in home.glob('*/index.rst') ]

###

#path.stat().st_size for path in home.glob('*/index.rst') 

list(path.stat().st_size for path in home.glob('*/index.rst'))

some_list = [None for i in range(100)]

###

sizes = list(path.stat().st_size 
    for path in home.glob('*/index.rst'))

sum(sizes)
max(sizes)
min(sizes)
from statistics import mean
round(mean(sizes), 3)
sizes.index(min(sizes))

###

ch1 = list(path.stat().st_size 
    for path in home.glob('ch_01*/*.rst'))
ch2 = list(path.stat().st_size 
    for path in home.glob('ch_02*/*.rst'))
len(ch1)
len(ch2)
final = ch1 + ch2
len(final)
sum(final)

###

final_ex = []
final_ex.extend(ch1)
final_ex.extend(ch2)
len(final_ex)
sum(final_ex)

###

p = [3, 5, 11, 13]
p.insert(0, 2)
print(p)
p.insert(3, 7)
print(p)