import unpacking
x, y, z = unpacking.good_code()

def bad_code(x, y, z):
	x = int(x)
	y = int(y)
	z = int(z)
	return x * y * z


def good_code(x, y, z):
	x, y, z = map(int, (x, y, z))
	return x * y * z

'''
map(type, list)
The map function takes two arguments - a type and a list.
This function converts each list item to a specific type (using str to int as an example)
'''

if __name__ == '__main__':
	volume = good_code(x, y, z)
	print(f'{volume=}')


