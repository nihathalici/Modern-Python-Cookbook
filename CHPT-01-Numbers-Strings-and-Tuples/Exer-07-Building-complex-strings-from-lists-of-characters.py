# Exer-07-Building-complex-strings-from-lists-of-characters

title = "Recipe 5: Rewriting an Immutable String"


from string import whitespace, punctuation

title_list = list(title)

colon_position = title_list.index(':')

del title_list[:colon_position + 1]

for position in range(len(title_list)):
    if title_list[position] in whitespace+punctuation:
        title_list[position] = '_'

title = ''.join(title_list)

title_list.insert(0, 'prefix')
print(''.join(title_list))
