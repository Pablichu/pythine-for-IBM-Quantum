

def prev(func):
	def check_it(*args, **kwargs):
		x = args[1]
		if not isinstance(x, list):
			print('Not a list')
			return None
		if not all(isinstance(e, (int, float)) for e in x):
			print('Not a number')
			return None
		return func(x)
	return check_it

class TinyStatistician:
	@prev
	def mean(x) -> float:
		'''Calcula la media'''
		return sum(x) / len(x)

	@prev
	def median(x) -> float:
		'''Calcula la mediana'''
		x.sort()
		total = len(x)
		if total % 2 == 0:
			return (x[int(total/2)] + x[int(total/2 -1)])  / 2
		else:
			return x[int(total/2)]

	@prev
	def quartiles(x) -> float:
		'''Calcula los cuartiles 1º y 3º'''

	
	@prev
	def var(x) -> float:
		'''Calcula la varianza'''


	@prev
	def std(x) -> float:
		'''Calcula la desviacion estandar'''
