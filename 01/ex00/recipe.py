

class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredientes, description, recipe_type):
		if cooking_lvl < 1 and cooking_lvl > 5:
			cooking_lvl = 1

		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredientes = ingredientes
		self.description = description
		self.recipe_type = recipe_type

	
	def __str__(self):
		'''Returns a string to print with all the recipe info'''
		txt = ''
		txt = 'Recipe: {self.name}\n\t'
		txt += '> Level -> {self.cooking_lvl}\n\t> Time -> {self.cooking_time}\n\t> Recipe type -> {self.recipe_type}\nDescription: {self.description}'
		txt += '> Ingredients: {self.ingredientes}\n\t'
		return txt

# name (str): nombre de la receta,
# cooking_lvl (int): rango de 1 a 5,
# cooking_time (int): en minutos (sin números negativos),
# ingredients (lista): lista de todos los ingredientes, cada uno representado por un string,
# description (str): descripción de la receta,
# recipe_type (str): puede ser “entrante”, “comida” o “postre”.

'salmorejo'
2
40
['tomate', 'aceite', 'pan']
'Es una crema servida habitualmente como primer plato.\nSe trata de una preparación tradicional de Córdoba.'
'entrante'