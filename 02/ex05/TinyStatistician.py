from math import sqrt

def prev(func):
	def check_it(self, x):
		if not isinstance(x, list):
			print('Not a list')
			return None
		return func(self, x)
	return check_it

class TinyStatistician:
	@prev
	def mean(self, x) -> float:
		'''Calcula la media'''
		return sum(x) / len(x)

	@prev
	def median(self, x) -> float:
		'''Calcula la mediana'''
		x.sort()
		total = len(x)
		if total % 2 == 0:
			return (x[int(total/2)] + x[int(total/2 - 1)])  / 2
		else:
			return x[int(total/2)]

	@prev
	def quartiles(self, x) -> list:
		'''Calcula los cuartiles 1º y 3º'''
		x.sort()
		total = len(x)
		quart = list()
		if total % 2 == 0:

			quart.append((x[total//4] + x[total//4 - 1])  / 2)
			quart.append((x[3*total//4] + x[3*total//4 - 1])  / 2)
		else:
			quart.append(x[(total + 1)//4 - 1])
			quart.append(x[(3*(total + 1))//4 - 1])
		return quart
	
	@prev
	def var(self, x) -> float:
		'''Calcula la varianza'''
		n = len(x)
		med = self.mean(x)
		total = 0.0
		for nb in x:
			total += (nb - med) ** 2
		total /= n
		return total

	@prev
	def std(self, x) -> float:
		'''Calcula la desviacion estandar'''
		val = self.var(x)
		return sqrt(val)