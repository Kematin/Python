#Переменные (не могут начанаться с цифор и знаков)
name = "Kematin"
age = 13
print(name)
print(age)

#int (число)
number = 5
#float (дробное число)
fnamber = 5.6
#str (строка)
name2 = "Rafael"
#bool (имеют только 2 значения False или True)
status = False


#Экранирование
print("Просто здравствуй \"просто как\" дела?")
print("Просто здравствуй 'просто как' дела")


#Перевод строки
print("Привет меня зовут\nРафаэль")


#Контатенация (Текст и переменная)
print("Привет, меня зовут " + name2 + "!")
print("Мне целых " + str(age) + " лет!")
print("Мой статус " + str(status))



wtn = input("Как тебя зовут? ")
years = input("Сколько тебе лет? ")
print("Привет, дорогой " + wtn + "\nТебе уже " + str(years) + " лет!")


#Вычесления
a = 5
b = 10
c = a + b
d = a - b
e = a * b
k = a / b
ac = a ** b
ab = b % 3 
print(c)
print(d)
print(e)
print(k)
print(ac)
print(ab)

#унарный минус, округление и число пи
o = 41
o = -o
print(o)

f = 7.42
print(round(f))
import math 
print(math.ceil(f))
print(math.floor(f))

import math
print(math.pi)

#Если 
a = float(input("Введите первое число: "))

b = float(input("Введите второе число: "))

what = input("Введите знак вычесления (+ -) : ")

if what == "+": 
	c = a + b
	print("Ответ " + str(c))
elif what == "-":
	c = a - b
	print("Ответ " + str(c))
else:
	print("Выбран неверный знак")

