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