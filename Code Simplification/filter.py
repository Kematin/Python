#is a lighter variation of comprehensions

def bad_code(names, letter):
	names_starts_a = list()
	for name in names:
		if name[0] == letter:
			names_starts_a.append(name)

	return names_starts_a

def good_code(names, letter):
	names_starts_a = filter(lambda name: name.startswith(letter), names)
	return names_starts_a

if __name__ == '__main__':
	names = ['Michel', 'Rock', 'Andrew', 'Laura', 'Anton']
	print(*good_code(names, 'R'))