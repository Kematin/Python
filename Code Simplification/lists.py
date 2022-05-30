#Correct list copying

def uncorrect(lst):
	new_list = lst
	new_list.append(63)
	return new_list, lst #both lists will return [1, 513, 136, 135, 64, 13, 63]
	

def correct(lst):
	new_list = lst[:]
	new_list.append(2)
	return new_list, lst #new_list return list with 2 and lst return list without 2


if __name__ == '__main__':
	nums = [1, 513, 136, 135, 64, 13]
	first, second = correct(nums)
	print(f'{first=}\n{second=}')