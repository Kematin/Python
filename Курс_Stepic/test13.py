def find_all(target, symbol):
	total = []
	for i in range(len(target)):
		if target[i] == symbol:
			total.append(i)
	return total
s = 'abcdabcaaa'
char = 'a'


print(find_all(s, char))




def merge(list1, list2):
    all_n = numbers1 + numbers2
    all_n.sort()
    return all_n
numbers1 = [1, 2, 6, 7]
numbers2 = [5, 7,1, 6, 1, 7]


print(merge(numbers1, numbers2))


#ВАЖНО - умный способ сортировки списков
def qiuck_sort(list1, list2):
    result = []
    p1 = 0  
    p2 = 0  
    while p1 < len(list1) and p2 < len(list2):  
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):   
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]    
    return result

list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = qiuck_sort(list1, list2)
print(list3)
print()


'''
Кроме функций, возвращающих числовые значения, 
можно писать и возвращающие логические, строковые и другие значения. '''

def even_number(num):
	if num % 2 == 0:
		return True
	else:
		return False


if even_number(13):
	print('Число чётное')
else:
	print('Число не чётное')
print()


def is_invalid(num):
	if num != 300 and num != 200 and num != 100:
		return True
	else:
		return False

model = int(input())

while is_invalid(model):
	print('Неккоректное число, допустимые: 100, 200, 300')
	model = int(input())
else:
	print('Введено корректное число')



'''
В Python в функциях можно возвращать несколько значений через запятую
return 1, 2, 3 и т.д.
'''

def get_powers(num):
	return num**2, num**3, num**4

a, b, c = get_powers(2)
print(a, b, c, sep='--')


def solve(a, b, c, d, e, f):
    x = (d * e - b * f)/(a * d - b * c)
    y = (a * f - c * e)/(a * d - b * c)
    return x, y

xysol, yosol = solve(2, 3, 4, 1, 2, 5)
print('Пересекаются по оси x', xysol, 'по оси y', yosol)