#Умножение строк
print("Привет" * 2)

name = input("Ваше имя : ")
l = input("Сколько раз умножить ваше имя?")
print(name * int(l))

#Увелечение и уменьшение переменных
t = 20
t = t+10
t += 10

a = 40
a = a - 20
a -= 20

b = 5
b *= 5

#Сравнение
print( 10 == 11)#Равно (если правда выведет True)
print( 10 != 11)#НЕ равно (если правда выведет True)
print( 10 > 4)#True
print( 10 > 20)#False
print ( 5 >= 5)#2 случая больше или равно в любых из них True, если меньше False

#Лексиграфические сравнения
#Test Определяется по весу букв, которые в свою очередь по алфавиту
#Tesa 
#test > tesa #64 > 45
print("afwajnaljwfa" > "awlaALfmae") #False

#Сдвоенные условия и множественные условия
pogoda = "Солнечная"
time = "День"
#if pogoda == "Солнечная":
#	if time == 'День'
#		print("Классная погода иди гулять!") = 
if pogoda == "Солнечная" and time == "День":
	print("Иди гулять!")
if pogoda == "Дождь" and time == "Вечер" or time == "Ночь":
	print("Иди поспи, а")

#Not
p = "Облачно"
if not p == "Облачно":
	print("что-то")
#if p != "Облачно"
	#print("что-то")           ( оба действия одинаковы ) 


#Приоритеты
#p1 = ()
#p2 = **
#p3 = * /
#p4 = + -


#Циклы ( для повторного выполнения условия )
test = 3

while test == 3:
	print("Текст")
	test += 1 
	#цикл окончается после не совпадения условий


i = 1

while i <= 10000:
	print(i)
	i += 1 

	if i == 5:
		break #автоматически остановится на 4



#Продолжить continue

number = 0 

while number <= 10:
	number += 1
	if (number % 2) != 0:
		continue;
	print("Четные числа = " + str(number))



#Списки 

nu = [1,2,3,10,140]
name = ["raf", "kem" , "lol4ka"]

print(nu[3])#Выведится число 10 т.к. оно третье по щёту (0, 1 , 2 , 3)
print(name[1])#Выведится kem

test2 = [5, 10, 5,[1, 5, 6,]]
print( test2 [3][2] )    
#Выведится 6

test3 = ["lol4ka", "kem", 'loh',["kaka", "jopa",["loh", "lol4ka",]]]
print(test3[3][2][1])


print( nu + [1, 2 , 3, 4,] ) # всё выведится в 1 список


#Проверка списка

nam = ["Rafael", "Abraham", "Mila"]
if "Rafael" in nam:
	print("Данное имя присутсвует в данном списке")
else:
	print("Данного имени нету в списке")

if "lol4ka" not in nam:
	print("Данного имени нету!")


#добавление в список

names = []

names.append("Rafael")
names.append([1, 8, 10, 149])
print(names)

names.append(input("Зарегестрируйте ваше имя "))
answer = input("Введите имя поиска ")
if answer == names:
	print("Данное имя есть в списке зарегестрированных")
else:
	print("Данного имени нет в списке зарегестрированных")



mol = [1,4,1,4,5,1,51,5,1,4,1,4,14,1,1,3,4,1]
print("В списке mol находиться " + str(len(mol)) + " чисел.") 

mol.remove(4) #Удаление объекта (всего может принять 1 аргумент)
print("После удаленния 4 в массиве mol " + str(len(mol)) + " элементов")


mol.insert(0, 130) #Добавляет элемент в определённый момент списка

print(max(mol)) #Выведится макс число из списка
print(min(mol)) #Обратная операция


print(mol.count(1)) #Сколько определённых элементов в списке (элемент 1 встречается 8 раз)


#как перевернуть массив
mol.reverse()
print(mol)


#Строки документирования


def hello():
	"""Описание функции"""
	print("Привет")

print(hello.__doc__) #Выведится док (т.е. "описание функции")

#В переменную можно внести функцию

hell = hello
print(hell) #Выведится Привет

#Функции можно передовать др функциям в качестве аргумента

def my_names(name):
	print("Привет, " + name() + "!!")

def your_name():
	return "###" + input("Ваше имя? ") + "###"
	
my_names(your_name)





