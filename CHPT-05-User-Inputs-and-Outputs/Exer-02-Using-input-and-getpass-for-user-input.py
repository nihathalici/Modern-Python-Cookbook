# Exer-02-Using-input-and-getpass-for-user-input

from datetime import date

def get_date():
    year = int(input("year: "))
    month = int(input("month [1-12]: "))
    day = int(input("day [1-31]: "))
    result = date(year, month, day)
    return result 

###

from getpass import getpass

###

month = None
while month is None:
    month_text = input("month [1-12]: ")
    try:
        month = int(month_text)
        if 1 <= month <= 12:
            pass
        else:
            raise ValueError("Month of range 1-12")
    except ValueError as ex:
        print(ex)
        month = None

###

input_date = None
while input_date is None:
    year = get_integer("year: ", 1900, 2100)
    month = get_integer("month [1-12]: ", 1, 12)
    day = get_integer("day [1-31]: ", 1, 31)
    try:
        result = date(year, month, day)
    except ValueError as ex:
        print(ex)
        input_date = None
# assert input_date is the valid date entered by the user

###

day_1_date = date(year, month, 1)
if month == 12:
    next_year, next_month = year+1, 1
else:
    next_year, next_month = year, month+1
day_end_date = date(next_year, next_month, 1)
