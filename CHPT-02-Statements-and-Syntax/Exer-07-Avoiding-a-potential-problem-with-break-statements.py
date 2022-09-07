# Exer-07-Avoiding-a-potential-problem-with-break-statements

sample_1 = "some_name = the_value"
for position in range(len(sample_1)):
    if sample_1[position] in '=:':
        break
print('name=', sample_1[:position],
       'value=', sample_1[position+1:])

sample_2 = 'name_only'
for position in range(len(sample_2)):
    if sample_2[position] in '=:':
        break
print('name=', sample_2[:position], 
      'value=', sample_2[position+1:])

###

position = -1 # If it's zero length
for position in range(len(sample_2)):
    if sample_2[position] in '=:':
        break

if position == -1:
    print("name=", None, "value=", None)
elif not(text[position] == ':' or text[position] == '='):
    print("name=", sample_2, "value=", None)
else:
    print('name=', sample_2[:position], 'value=', sample_2[position+1:])

###

if len(sample_2) > 0:
    name, value = sample_2, None
else:
    name, value = None, None

for position in range(len(sample_2)):
    if sample_2[position] in '=:':
        name, value = sample_2[:position], sample_2[position:]
print('name=', name, 'value=', value)

###

for position in range(len(sample_2)):
    if sample_2[position] in '=:':
        name, value = sample_2[:position], sample_2[position+1:]
        break
else:
    if len(sample_2) > 0:
        name, value = sample_2, None 
    else:
        name, value = None, None
