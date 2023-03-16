cookbook={
	'bocadillo' : {
		'ingredients' : ["jamón", "pan", "queso", "tomate"],
		'meal' : "almuerzo",
		'prep_time' : 10
	},
	'tarta' : {
		'ingredients' : ["harina", "azúcar", "huevos"],
		'meal' : "postre",
		'prep_time' : 60
	},
	'ensalada' : {
		'ingredients' : ["aguacate", "rúcula", "tomates", "espinacas"],
		'meal' : "almuerzo",
		'prep_time' : 15
	}
}

def cookbook__list():
	print(' >> In this cookbook we have ' + str(len(cookbook)) + ' recipes: ')
	for x in cookbook:
		print('\t- ' + x)

def cookbook__showRecipe(name = None):
	if name is None:
		print(' >> No recipe gave?')
		return

	try:
		print(' >> For ' + name + ', which is a ' + cookbook[name]['meal'] + ', we need:')
		for x in cookbook[name]['ingredients']:
			print('\t- ' + x)
		print('\t Time to prepare -> ' + str(cookbook[name]['prep_time']))
	except:
		print(' >> This recipe do not exits!')

def cookbook__deleteRecipe(name = None):
	if name is None:
		print(' >> No recipe gave?')
		return

	try:
		del cookbook[name]
		print(' >> ' + name + ' has been removed!')
	except:
		print(' >> This recipe do not exits!')

def cookbook__addRecipe():
	try:
		name = input('>>> Enter a recipe name: ')
		ingredients = []
		print('>>> Enter ingredients: ')
		while True:
			new_ingredients = input('\t> ')
			if new_ingredients is '':
				break
			ingredients.append(new_ingredients)
		meal = input('>>> Insert meal type: ')
		time = input('>>> Enter preparation time: ')

		new_recipe ={
			'ingredients' : ingredients,
			'meal' : meal,
			'prep_time' : int(time)
		}
		cookbook[name] = new_recipe
	except:
		print(' >> An error has ocurred!!')

if __name__ == '__main__':
	print('Welcome to the Python Cookbook!')
	print('List of available option:')
	print('\t1: Add a recipe')
	print('\t2: Delete a recipe')
	print('\t3: Print a recipe')
	print('\t4: Print the cookbook')
	print('\t5: Quit')

	while True:
		option = int(input(' > Select an option: '))
		if option == 1:
			cookbook__addRecipe()
		elif option == 2:
			cookbook__deleteRecipe(input('\t > Insert recipe to delete: '))
		elif option == 3:
			cookbook__showRecipe(input('\t > Insert which recipe to show: '))
		elif option == 4:
			cookbook__list()
		elif option == 5:
			break
		else:
			print('WTF HAVE YOU INSERT? CMON BROOOO')
	print('BYEEEEEEE')


