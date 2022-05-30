from functools import reduce

def previous_code():
	x, y, z = map(int, input().strip().split())
	return x * y * z


def quick_code():
	return reduce(
		lambda x, y: x * y,
		map(int, input().strip().split())
		)

'''
But this code is difficult to understand
'''


if __name__ == '__main__':
	volume = quick_code()
	print(f'{volume=}')