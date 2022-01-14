def bad_code():
	numbers = input()
	numbers.strip()
	numbers.split()
	x = numbers[0]
	y = numbers[1]
	z = numbers[2]
	print(f'{x}\n{y}\n{z}')

def good_code():
	x, y, z = input().strip().split()
	return x, y, z

if __name__ == '__main__':
	x, y, z = good_code()
	print(f'{x=}\n{y=}\n{z=}')


