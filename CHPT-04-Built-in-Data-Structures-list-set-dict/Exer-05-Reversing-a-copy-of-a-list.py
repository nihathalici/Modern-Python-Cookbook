# Exer-05-Reversing-a-copy-of-a-list

week = 13
day = 2
hour = 7
minute = 53
second = 19
t_s = (((week*7+day)*24+hour)*60+minute)*60+second
#print(t_s)

###

t_s = 8063599
fields = []
for b in 60, 60, 24, 7:
    t_s, f = divmod(t_s, b)
    fields.append(f)
fields.append(t_s)
print(fields)

###

fields_copy1 = fields.copy()
fields_copy1.reverse()
print(fields_copy1)

fields_copy2 = fields[::-1]
print(fields_copy1)