#Матрицы

#Перебор по столбцам
def get_by_pillar():
	rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов

	matrix  = [[2, 3, 1, 0],
	           [9, 4, 6, 8],
	           [4, 7, 2, 7]]

	for c in range(cols):
	    for r in range(rows):
	        print(matrix[r][c], end=' ')
	    print()


#Перебор по строкам
def get_by_string():
	rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов

	matrix  = [[2, 3, 1, 0],
	           [9, 4, 6, 8],
	           [4, 7, 2, 7]]

	for r in range(rows):
	    for c in range(cols):
	        print(matrix[r][c], end=' ')
	    print()


#ljust(), rjust()

'''
Строковый метод ljust() выравнивает текст по ширине, добавляя пробелы в конец текста.
Строковый метод rjust() выравнивает текст по ширине, добавляя пробелы в начало текста.
'''

def all_just():
	print('a'.rjust(3))
	print('ab'.rjust(3))
	print('abc'.rjust(3))

	print('abcdefg'.rjust(10, '~').ljust(13, '~'))

	rows, cols = 3, 4			# rows - количество строк, cols - количество столбцов
	matrix  = [[277, -930, 11, 0],
	           [9, 43, 6, 87],
	           [4456, 8, 290, 7]]
	for c in range(cols):
		for r in range(rows):
			print(str(matrix[r][c]).ljust(6), end='')
		print()



#Квадратные матрицы
def square_matrix(withd):
	matrix = [[0]*withd for _ in range(withd)]     #Создание квадратной сетки

	for i in range(withd):
		matrix[i][i] = 1           #Изменение значений
		matrix[i][withd-i-1] = 2


	for c in range(withd):
		for r in range(withd):			#Метод матрицы
			print(matrix[r][c], end=' ')
		print()




#Примечание 2. Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:
def print_matrix(matrix, n, width=1):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()



#Примечание 3. Для считывания матрицы из n строк, заполненной числами, удобно использовать следующий код:
def check_3():
	n = int(input())
	matrix = []
	for i in range(n):
	    temp = [int(num) for num in input().split()]
	    matrix.append(temp)




def first(rows, cols):
	names = [input() for _ in range(rows * cols)]

	matrix = list()
	count = 0
	flag = cols
	for _ in range(rows):
		matrix.append(names[count:cols])
		count += flag
		cols += flag

	for item in matrix:
		print(*item)
	print()


first(int(input()), int(input()))