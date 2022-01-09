#Pass - ничего не делает, для пустой функции
def pustota():
	pass

if 120 >= 41:
	pass #ничё не будет


#Кортёж (ang. Tuple)

years = (5, 3, 6, 10, 20)  #years = 4, 6, 7, 10       #Tuple (по сути переменная :D)
print(years[2])



number = [1,2,3,4,5]
number[2] = 10                    #List
number.insert(1, 20)
print(number[2])



names = {                     #Dictionary
	"Агишев" : "Рафаэль",
	"Мурас" : "Александра",
	"Лагерев" : "Арсений"                           
}	
print(names.get("Агишев", "Человека нет в списке"))


#В отличие от других Tuple не может видоизменятся, хоть и имеет тот же синтакс что и лист


#Срез спиской (List indexing)


chisla = [1,2,3,4,5,6,8]
print(chisla[1:5])               #Элемент с индексом 5 не выведится, т.к. он заканчивает действие (как range)

for nn in chisla:
	if nn <= 5 and nn >= 2:
		print(nn)
	nn += 1


print(chisla[:6])      #Выведется всё от начала до элемента с индексом 6 (8)
print(chisla[1:])      #Выведется всё начиная с элемента под индексом 1 (2)


print(chisla[0:6:2])   #3 аргумент означает через сколько шагов делать вывод (1, 3, 5)
print(chisla[::3]) #1, 4, 8


chisla2 = range(2, 10)[::2]

for i in chisla2:
	print(i)




print(chisla[-2]) #выведится число с конца, при том, что индекс меняется и уже 8 = -1, а не 0
print(chisla[-5:-2]) #Равноценно print(chisla[2:5])
print(chisla[-2:-7:-1]) #Что-бы сделать от конца к началу


print(chisla[::-1][::-1]) #Будем сново от начала к концу 



#Форматирование строк

name = "raf"
age = 23
# %
# .format()

print("Привет, %s!\nТебе уже %d лет" % (name, age))

# %s - плейсхолдер строки 
# %d - плейсхолдер числа 
# %f - плейсхолдер дроби 
del name
del age


name = "Рафаэль"
age = 12
print("Привет, {}!\nТебе уже {} лет".format(name, age))

print("{0} {1} {2}".format("раф", "лол", 23))
#Всё ставится под своим индексом 

del name
del age


name_1 = "loh"
age_1 = 21
print("Привет, {name}! тебе уже {age} лет!".format(name = name_1, age = age_1)) 



humans = {
	"name" : "Raf",
	"age" : 32

}
print('Привет {human[name]}! тебе уже {human[age]} лет!'.format(human = humans))


str_men = "loh"

#loh____ = "<"
#_____loh = ">"
#___loh___ = "^"
print( ('{0:#^6}').format(str_men))


le = 6

print("Результат деления по модулю - "  + str(len(str_men) % 2))

if(len(str_men) % 2):
	le += 1

print( ('{0:#^'+str(le)+'}').format(str_men))





#join, min, max, replace, startswith, endswith, lower, upper, split, abs, sum
fruits = ["Мандарин", "Апельсин", "Яблоко", "Ананас"]
goroda = "Сургут , Москва , Санкт-Петербург"


print(' & '.join(fruits))
'''Создаёт из списка или кортежа строку
по какому либо признаку'''


print('Привет, имя!'.replace('имя', 'Дмитрий')) 
'''Меняет элемент'''


name = input('Ваше имя: ')
if(name.startswith('А')):
	print('Вы элитный А (0-0)')
else:                                
	print('Вы не элита(((')
'''Проверяет с чего начинается текст'''



if(name.lower().startswith('а')):
	print('Вы элитный А (0-0)')
else:                                
	print('Вы не элита(((')	
'''Переводит строку в нижний регистр
например ПРИВЕТ - привет'''


del name
h = input("? ")
if(h.lower().endswith('а')):
	print("А")
else:
	print('Не а')
'''Обратный эффект startswith'''



print(h.upper())
'''Переводит всё в верхний регистр
привет - ПРИВЕТ'''


print(goroda.split(' , '))
'''Создаёт из строки лист
по признаку в функции'''


print(min(fruits))
print(max(fruits))
'''Выводят минимальный и 
максимальный элемент'''


print(abs(-312))
'''Создаёт абсолютное число
(число без каких либо знаков)'''


print(sum([3,1,4,51,5]))
'''Суммирует все числа'''