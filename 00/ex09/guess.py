from random import randint
import sys

print('GUESSING TIME YOU FUCKER!!')
print('From 0 to 100 you have to find the secret numer.')
print('If you cannot keep up with it, type "exit".')
print('Good luck, hf!')

tries = 0
nb = randint(1, 99)
while True:
	print('Type a number: ')
	try:
		inputed = input('\t>> ')
		if inputed == 'exit':
			tries = -1
			break
		typed = int(inputed)
	except:
		print('Not a number')
		tries += 1
		continue

	if typed <= 0 and typed >= 100:
		print("BETWEEN 0 and 100...")
	elif typed < nb:
		if (nb - typed) <= 10:
			print('Low!')
		else:
			print('Too low')
	elif typed > nb:
		if (typed - nb) <= 10:
			print('High!')
		else:
			print('Too high')
	else:
		break
	tries += 1
	print()

if tries == -1:
	print('Bye then loser')
	sys.exit()

if not tries:
	print('AMAZING!! JUST ONE TRY WOOOW <3')
else:
	print('Yey well done, you just needed ' + str(tries) + ' tries...')
if nb == 42:
	print('"I love deadlines. I love the whooshing noise they make as they go by."')
