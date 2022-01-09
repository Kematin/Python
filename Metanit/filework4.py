'''
Ряд возможностей по работе с каталогами и файлами предоставляет встроенный модуль os. 
Хотя он содержит много функций, рассмотрим только основные из них:

mkdir(): создает новую папку

rmdir(): удаляет папку

rename(): переименовывает файл

remove(): удаляет файл
'''

from os import *

'''
 путь относительно текущего скрипта
os.mkdir("hello")
'''

# абсолютный путь
mkdir("D://Python//Metanit//Тест папка")


''' 
путь относительно текущего скрипта
os.rmdir("hello")
'''

# абсолютный путь
rmdir("D://Python//Metanit//Тест папка")

#Мини программа

def program():
	answer = input('Привет! ты хочешь создать новую папку или удалить старую? Введи + если создать и - если удалить ')

	if answer == '+':
		name = input('Введите название папки: ')
		place = input('Введите место создание папки: ')
		place += name
		mkdir(place)

	elif answer == '-':
		name = input('Введите название папки: ')
		place = input('Введите место создание папки: ')
		place += name
		rmdir(place)

	else:
		print('Ещё увидимся!')

def remove_files():
	rename('D://Python//Metanit/testfilework2.txt', 'D://Python//Metanit/testfilework3.txt')
	remove('D://Python//Metanit/testfilework3.txt')

#Существование файла - os.path.exists(path)

print(path.exists('testfilework3'))

#Мини программа 


def true_files_or_false(file):
	file += '.txt' #или += 'dat' += 'py' и т.д.

	if path.exists(file) == True:
		print('Файл существует')
		pass 
		#какие либо операции
	else:
		print('Файла не существует')
		pass 
		#какие либо действия

