# Exer-01-Choosing-a-data-structure

valid_inputs = {"yes", "y", "no", "n"}
answer = None
while answer not in valid_inputs:
    answer = input("Continue? [y, n] ").lower()

valid_inputs.add("y")
print(valid_inputs)

###

month_name_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_name_list[8]
month_name_list.index("Feb")

###

scheme = {"Crimson": (220, 14, 60), "DarkCyan": (0, 139, 139), "Yellow": (255, 255, 00)}
print(scheme['Crimson'])