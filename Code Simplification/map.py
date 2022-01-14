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


volume = good_code(x, y, z)
print(f'{volume=}')


