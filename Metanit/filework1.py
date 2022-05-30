'''
Открытие файла с помощью метода open()

Чтение файла с помощью метода read() или запись в файл посредством метода write()

Закрытие файла методом close()
'''

#open(filename, mode (r, w, a, rb, wb))


file = open('тест.txt', 'w')
file.close()

'''
При открытии файла или в процессе работы с ним мы можем столкнуться 
с различными исключениями, например, к нему нет доступа и т.д. 
В этом случае программа выпадет в ошибку, а ее выполнение не дойдет до вызова метода 
close, и соответственно файл не будет закрыт.
'''

#with используется для удобство и предворительного закрытия файла

with open('тест.txt', 'w') as myfile:
	#какие либо действия
	pass 


#запись в файл с помощью w (write) or a (append)


with open('тест.txt', 'w') as file1:
	file1.write('Ты лучший!')

with open('тест.txt', 'a') as file:
	file.write('\nИ крутой!')

#Еще один способ записи в файл представляет 
#стандартный метод print(), который применяется для вывода данных на консоль:

with open('тест.txt', 'a') as file:
	print("\nHello world!", file=file)


'''
Для чтения файла он открывается с режимом r (Read), 
и затем мы можем считать его содержимое различными методами:

readline(): считывает одну строку из файла

read(): считывает все содержимое файла в одну строку

readlines(): считывает все строки файла в список
'''

with open('тест.txt', 'r') as file:
	for line in file:
		print(line, end='')


with open('тест.txt', 'r') as file:
	str1 = file.readline()
	print(str1, end='')
	str2 = file.readline()


with open('тест.txt', 'r') as file:
	lst = file.readlines()
	print('\n', lst[0], lst[1], lst[2], sep='')


'''
При чтении файла мы можем столкнуться с тем, что его кодировка не совпадает с ASCII. 
В этом случае мы явным образом можем указать кодировку с помощью параметра encoding:

filename = "hello.txt"
with open(filename, encoding="utf8") as file:
    text = file.read()
'''


filename = input('Введите желаемое название файла ')
filename += '.txt'

text = [input('Текст - ') for line in range(int(input('Кол-во строк текста - ')))]


with open(filename, 'w') as file:
	for line in text:
		file.write(line)
		file.write('\n')


with open(filename, 'r') as file:
	print('Вот ваш текст')
	lst = file.readlines()

	for line in lst:
		print(line, end='')
