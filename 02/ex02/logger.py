import time
from random import randint
import os


def log(func):
	def wrapper(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		execution_time = time.time() - start_time
		func_name = func.__name__.replace('_', ' ').title()
		with open('machine.log', 'a') as f:
			if execution_time < 1:
				time_unit = 'ms'
				execution_time *= 1000
			else:
				time_unit = 's '
			f.write(f'(cmaxime)Running: {func_name:18} [ exec-time = {execution_time:.3f} ' + time_unit + ' ]\n')
		return result
	return wrapper		

#logging.info(f"cmaxime - {func.__name__} - Execution time: {execution_time:.5f} seconds")


class CoffeeMachine():
	
	water_level = 100
	
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False
	
	@log
	def boil_water(self):
		return "boiling..."
	
	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	try:
		os.remove("machine.log")
	except FileNotFoundError:
		pass

	machine = CoffeeMachine()
	
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)