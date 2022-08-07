# Exer-02-Choosing-between-float-decimal-and-fraction

from decimal import Decimal

tax_rate = Decimal('7.25')/Decimal(100)
purchase_amount = Decimal('2.95')
print(tax_rate * purchase_amount)

penny = Decimal('0.01')
total_amount = purchase_amount + tax_rate * purchase_amount
print( total_amount.quantize(penny) )

import decimal
print( total_amount.quantize(penny, decimal.ROUND_UP) )
