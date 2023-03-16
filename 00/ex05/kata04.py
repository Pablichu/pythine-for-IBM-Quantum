# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

from decimal import Decimal

print('module_0{mod}, ex_0{ex} : {dec}, {enter:.2e}, {deci:.2e}'
.format(mod=kata[0], ex=kata[1], dec=round(kata[2], 2), enter=Decimal(kata[3]), deci=Decimal(kata[4])))
