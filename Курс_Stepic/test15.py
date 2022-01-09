from random import *

num1 = randint(0, 10) #Случайное число 
print(num1)

num2 = randrange(0, 100, 5) #Случайное число с цикла 
print(num2)

num3 = random() #Возрващает дробное число в диапозоне 0 - 1
print(num3)

num4 = uniform(1.2, 5.6) #Возвращает случайное дробное число
print(num4) 


from random import *

#random.seed(10)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(randint(1, 20))

#При повторном запуске кода будут появляться те же 'случайные' числа

print('Бросаем кубик \n','Выпало значение:', randint(1, 6))
print()


count = 0
again = 'да'
while again.lower() == 'да':
	print('Брося кубика выпало значение')
	print('--' + str(randint(1, 6)) + '--')
	again = input('Хотите бросить ещё раз? (введите да если хотите)')
	count += 1
else:
	print('Вы закончили бросать кубик, всего раз вы его бросили', count)



for _ in range(5):
	num = randint(0, 1)
	if num == 0:
		print('Орёл')
	else:
		print('Решка')