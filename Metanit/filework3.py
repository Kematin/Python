'''
Бинарные файлы в отличие от текстовых хранят информацию в виде набора байт. 
Для работы с ними в Python необходим встроенный модуль pickle.
Этот модуль предоставляет два метода:

dump(obj, file): записывает объект obj в бинарный файл file

load(file): считывает данные из бинарного файла в объект
'''

from pickle import *

name_file = 'test.dat'
age = 14
name = 'raf'

with open(name_file, 'wb') as file:
	dump(age, file)
	dump(name, file)

with open(name_file, 'rb') as file:
	age_person = load(file)
	name_person = load(file)
	print(name_person, '-', age_person, 'age')


filename = 'users.dat'

users = [
['Tom', 13],
['Maria', 15],
['Dima', 20]
]

with open(filename, 'wb') as file:
	dump(users, file)

with open(filename, 'rb') as file:
	users = load(file)
	for person in users:
		print('Имя -', person[0], person[1], 'Лет')