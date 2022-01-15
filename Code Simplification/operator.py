def bad_code(name, lst):
	#first
	if name == 'Andrew' or name == 'Michel' or name == 'He': print(name)

	#second
	a, b, c, d, e = lst
	if a and b and c and d and e: print('all is True') 
	else: print('all numbers isn`t True')

	#third
	if a or b or c or d or e: print('any True')
	else: print('all if False')



def good_code(name, lst):
	#first (in)
	if name in ('Andrew', 'Michel', 'He'): print(name)

	#second (all)
	if all(lst): print('all is True') 
	else: print('all isn`t True')

	
	#third (any)
	if any(lst): print('any True')
	else: print('all is False')


if __name__ == '__main__':
	name = 'Andrew'
	lst = [True for _ in range(5)]
	lst.append(False)
	good_code(name, lst)