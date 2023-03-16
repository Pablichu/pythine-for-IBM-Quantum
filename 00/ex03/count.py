import sys

def text__analyzer(phrase = None):
	"""This is a function that counts all characters, upper letters, lower letters,
punctuation marks and spaces. If no string is given it will asks to inputa string"""

	if phrase is None:
		print('Cool, what do you want to analyze?')
		phrase = input(">> ")

	if not isinstance(phrase, str):
		print('Not a phrase so not working!')
		sys.exit()
	
	chars = len(phrase)
	upper = int(0)
	lower = int(0)
	marks = int(0)
	space = int(0)

	for x in phrase:
		if x.isupper():
			upper += 1
		elif x.islower():
			lower += 1
		elif x in ['!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"]:
			marks += 1
		elif x in ' ':
			space += 1

	print('Text contains ' + str(chars)	 + ' character(s):')
	print('- ' + str(upper) + ' upper letter(s)')
	print('- ' + str(lower) + ' lower letter(s)')
	print('- ' + str(marks) + ' puntuation mark(s)')
	print('- ' + str(space) + ' space(s)')

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('No way you haven\'t given an argument or have given too much. So not valid D:')
		sys.exit()
	text__analyzer(sys.argv[1])