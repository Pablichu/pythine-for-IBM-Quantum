from random import randint

# function prototype
def generator(text, sep=" ", option=None):
	'''Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
	   option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
	   shuffle: mezcla la lista de palabras,
	   unique: devuelve una lista de palabras donde cada palabra solo aparece una vez
	   ordered: ordena alfabéticamente las palabras.
	'''

	words = text.split(sep)
	if option == None:
		for s in words:
			yield s
	elif option == 'shuffle':
		while len(words):
			rand = randint(0, len(words) - 1)
			yield words[rand]
			words.pop(rand)
	elif option == 'unique':
		unique = list()
		for s in words:
			if s not in unique:
				unique.append(s)
				yield s
	elif option is 'ordered':
		while len(words):
			check = words[0]
			for s in words:
				if check > s:
					check = s
			words.remove(check)
			yield check
	else:
		print('Not a valid option')
	return

if __name__ == "__main__":
	
	text = "Le de Lorem Ipsum est simplement du faux texte. cara cara cara cara caa"
	
	print('\n >> Now None!\n')
	for word in generator(text, sep=" "):
		print(word)
	
	print('\n >> Now shuffle!\n')
	for word in generator(text, sep=" ", option="shuffle"):
		print(word)
	
	print('\n >> Now unique!\n')
	for word in generator(text, sep=" ", option="unique"):
		print(word)
	
	print('\n >> Now ordered!\n')
	for word in generator(text, sep=" ", option="ordered"):
		print(word)
