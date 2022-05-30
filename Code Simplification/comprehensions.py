def bad_code(names):
	names_starts_a = list()
	for name in names:
		if name[0] == 'A':
			names_starts_a.append(name)

	return names_starts_a

def good_code(names):
	names_starts_a = [name for name in names if name.startswith('A')]
	return names_starts_a


if __name__ == '__main__':
	names = ['Michel', 'Rock', 'Andrew', 'Laura', 'Anton']
	print(*good_code(names))
