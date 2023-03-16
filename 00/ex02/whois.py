import sys

string = 'AssertionError: '
if len(sys.argv) != 2:
	if len(sys.argv) > 2:
		print(string + ' too many arguments')
	else:
		print(string + ' no argument')
	sys.exit()

if not isinstance(sys.argv[1], int):
	print(string + ' Not an integer')
	sys.exit()

nb = int(sys.argv[1])
if nb is 0:
	print('Definetly I\'m ZERO')
elif nb % 2:
	print('I\'m ODD')
else:
	print('I\'m EVEN')