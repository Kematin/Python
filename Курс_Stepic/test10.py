'''
Метод insert()
Метод index()
Метод remove()
Метод pop()
Метод reverse()
Метод count()
Метод clear()
Метод sort()
'''

#инсерт - вставляет в определённый индекс, какое либо значение
names = ['Raf', 'Angelina', 'Dima']
names.insert(1, 'Sasha')
print(names)


#индекс - выводит индекс значения, заданного в нём, если его нет, выведет -1
names = ['Raf', 'Angelina', 'Dima']
print(names.index('Dima'))


#римув - удаляет определённый символ
names = ['Raf', 'Angelina', 'Dima']
names.remove(names[1]) #Можно задать значени, а не индекс
print(names)


#поп - удаляет из списка элемент и возвращает его
names = ['Raf', 'Angelina', 'Dima']
raf = names.pop(0)
print(raf)
print(names)


#коунт - выводит сколько раз встречается значение в листе
names = ['Raf', 'Angelina', 'Dima']
print(names.count('Raf'))


#реверсе - переворачивает список
names = ['Raf', 'Angelina', 'Dima']
names.reverse()
print(names)


#клеар - удаляет все элементы списка
names = ['Raf', 'Angelina', 'Dima']
names.clear()
print(names)


#Сорт - сортирует список
nums = [-1, 0, -13, 1, 90, 0, -13413, 139]
nums.sort()
print(nums)

'''
По умолчанию метод sort() сортирует список по возрастанию. 
Если требуется отсортировать список по убыванию, 
необходимо явно указать параметр reverse = True.
'''

nums.sort(reverse=True)
print(nums)



'''
Примечание. 
Существует большая разница в работе строковых и списочных методов. 
Строковые методы не изменяют содержимого объекта к которому они применяются, 
а возвращают новое значение. 
Списочные методы, напротив, меняют содержимое объекта к которому применяются.
'''




