# Exer-03-Input-string-parsing

import datetime

raw_date_str = input("date [yyyy-mm-dd]: ")
input_date = datetime.strptime(raw_date_str, '%Y-%m-%d').date()
