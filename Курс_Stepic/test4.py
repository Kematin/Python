'''
Частые сценарии range
1 - Подсчет количества
2 - Вычисление суммы и произведения
3 - Обмен значений переменных
4 - Сигнальные метки
5 - Максимум и минимум
'''
#1
counter = 0
for i in range(3):
    num = int(input())
    if num > 10:
        counter = counter + 1
print('Было введено', counter, 'чисел, больших 10.')


#2.1
total = 0
for i in range(3):
    num = int(input())
    if num > 10:
        total = total + num
print('Сумма чисел больших 10 равна',  total)

#2.2
total = 0
for i in range(1, 101):
    total = total + i
print('Сумма равна', total)

#2.3
total = 0
for i in range(3):
    num = int(input())
    total = total + num
average = total / 10
print('Среднее значение равно', average)



#3.1
x = 5
y = 3
temp = x
x = y
y = temp

#3.2
x, y = y, x



#4
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False

if num != 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

#5.1
largest = -1
for i in range(3):
    num = int(input())
    if num > largest:
        largest = num
print('Наибольшее число равно', largest)

#5.2
largest = 1000
for i in range(3):
    num = int(input())
    if num <= largest:
        largest = num
    elif num > 1000:
        print('Не вводи число больше 1000')
print('Наименьшее число равно', largest)

