#Функции 

'''
def название_функции():
    блок кода
'''

'''
 Иногда, при объявлении функции требуется сделать своего рода заглушку, 
 чтобы функция ничего не выполняла. Тогда мы используем ключевое слово pass: 

def do_nothing():
    pass
'''

def draw_box():
	for i in range(1, 6):
		print('*' * i)
draw_box()
print()
draw_box()



def print_message():
	print('Я король', end=' ')
	print('Артур')
print_message()


def draw_box():
    print('*' * 10)
    for _ in range(12):
    	print('*', '*', sep='        ')
    print('*' * 10)
draw_box() 


print()

def draw_triangle():
	print(*['*' * i for i in range(1, 11)], sep='\n')

draw_triangle()  




#Функции с параметрами

'''
def название_функции(параметры):
    блок кода
'''
print()
def draw_box(heigth, weight):
	for _ in range(heigth):
		print('*' * weight)

draw_box(5, 5)


def print_text(txt, count):
	print(txt * count)

print_text('OMG ', 5)


def draw_box_zero(heigth, weight, zero):
	print('*' * weight)
	for _ in range(heigth - 2):
		print('*', '*', sep=zero)
	print('*' * weight)
draw_box_zero(10, 10, '        ')



#Функции с возвратом значение

'''
def название_функции():
    блок кода
    return выражение
'''

def convert_to_c(temp):
	result = (5 / 9) * (temp - 32)
	return result

tp = 35
print(convert_to_c(tp))


def len_2(txt):
	total = 0
	for i in range(len(txt)):
		total += 1
	return total

print('Длинна строки - лошара', len_2('лошара'))


def balls(bal):
	if bal >= 90:
		return 5
	elif bal >= 75:
		return 4
	elif bal >= 40:
		return 3
	elif bal >= 20:
		return 2
	else:
		return 'Не сдал'

bal = int(input('Количество баллов: '))
print('Оценка -', balls(bal))


def compute_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c


def get_distance(x1, y1, x2, y2):
	return compute_hypotenuse(x1 - x2, y1 - y2)

print('Дистанция 5 3 8 5 равна:', get_distance(5, 3, 8, 5))


