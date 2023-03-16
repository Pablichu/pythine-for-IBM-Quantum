import sys

if len(sys.argv) > 3:
	print('Brooo too many arguments!!')
	sys.exit()
if len(sys.argv) < 3:
	print('Usage: python operations.py <number1> <number2>')
	print('Example: python operations.py 10 5')
	sys.exit()

try:
	nb1 = int(sys.argv[1])
	nb2 = int(sys.argv[2])
except:
	print('Not a number')
	sys.exit()

print('Sum: ' + str(nb1 + nb2))
print('Difference: ' + str(nb1 - nb2))
print('Product: ' + str(nb1 * nb2))
if nb2 is 0:
	print('Quotient: ' + 'ERROR (division by zero)')
	print('Reaminder: ' + 'ERROR (modulo by zero)')
	sys.exit()

div = nb1 / nb2
res = nb1 % nb2
print('Quotient: ' + str(div))
print('Reaminder: ' + str(res))