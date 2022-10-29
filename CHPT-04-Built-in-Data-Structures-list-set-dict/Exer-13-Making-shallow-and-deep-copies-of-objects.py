# Exer-13-Understanding-variables-references-and-assignment

#a = b
some_dict = {'a': [1, 1, 2, 3]}
another_dict = some_dict.copy()
print(another_dict)

some_dict['a'].append(5)
print(another_dict)

print( id(some_dict['a']) == id(another_dict['a']) )

###

some_list = [[2, 3, 5], [7, 11, 13]]
another_list = some_list.copy()
print(some_list is another_list)
print(some_list[0] is another_list[0])

###

import copy

some_dict = {'a': [1, 1, 2, 3]}
another_dict = copy.deepcopy(some_dict)

some_dict['a'].append(5)
print(some_dict)
print(another_dict)

print( id(some_dict['a']) == id(another_dict['a']) )

###

copy_of_list = [item for item in some_list]
copy_of_dict = {key:value for key, value in some_dict.items()}

###

"""
immutable = (numbers.Number, tuple, str, bytes)
def deepcopy_list(some_list):
    copy = []
    for item in some_list:
        if isinstance(item, immutable):
            copy.append(item)
        else:
            copy.append(copy.deepcopy(item))
"""

a = [1, 2, 3]
a.append(a)
print(a)
