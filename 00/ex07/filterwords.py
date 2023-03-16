import sys

if len(sys.argv) != 3:
	print('Put the right number of arguments: -> 2 <-')
	sys.exit()

try:
	nb = int(sys.argv[2])
except:
	print('Not a numuber')
	sys.exit()

tupla = sys.argv[1].split(' ')
passed = [x for x in tupla if len(x) > nb]

print(passed)
