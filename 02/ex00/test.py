from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
from functools import reduce

if __name__ == '__main__':
	# Example 1:
	x = [1, 2, 3, 4, 5]
	
	print(' ORIGINAL: ')
	print(map(lambda t: t + 1, x))
	print(x)
	print('')
	print(' MINE: ')
	print(ft_map(lambda t: t + 1, x))
	print(x)
	print('\n--------------------\n')
	# Output:
	#[2, 3, 4, 5, 6]
	
	# Example 2:
	# Output:
	print(' ORIGINAL: ')
	print(filter(lambda dum: not (dum % 2), x))
	print(x)
	print('')
	print(' MINE: ')
	print(ft_filter(lambda dum: not (dum % 2), x))
	print(x)
	print('\n--------------------\n')
	# Output:
	#[2, 4]
	
	# Example 3:
	lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
	
	print(' ORIGINAL: ')
	print(reduce(lambda u, v: u + v, x))
	print(x)
	print('')
	print(' MINE: ')
	print(ft_reduce(lambda u, v: u + v, x))
	print(x)
	
	# Output:
	##"Hello world"