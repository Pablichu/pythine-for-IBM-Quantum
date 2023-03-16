from inspect import isfunction

def ft_reduce(function_to_apply, iterable):
	"""Apply function of two arguments cumulatively. Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator). Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function. """

	if not isfunction(function_to_apply):
		print(' >> Not a function')
		return None
	try:
		value = None
		for	itera in iterable:
			if value == None:
				value = itera
			else:
				value += itera
		return value
	except:
		print(' >> oooooooh ma god')
		return None
