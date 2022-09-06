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
