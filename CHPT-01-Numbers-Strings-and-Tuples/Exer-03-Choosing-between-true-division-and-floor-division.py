# Exer-03-Choosing-between-true-division-and-floor-division

total_seconds = 7385
hours = total_seconds//3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds//60
seconds = remaining_seconds % 60

print(hours, minutes, seconds)

# the alternative, using the divmod()

total_seconds = 7385
hours, remaining_seconds = divmod(total_seconds, 3600)
minutes, seconds = divmod(remaining_seconds, 60)
print(hours, minutes, seconds)
