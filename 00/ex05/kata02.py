# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

import datetime

print(str(datetime.datetime(*kata))[:-3:])