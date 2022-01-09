'''
Функция ord позволяет определить код некоторого 
символа в таблице символов Unicode. 
Аргументом данной функции является одиночный символ.
'''

numA = ord('A')
numB = ord('B')
numC = ord('C')
print(numA, numB, numC, sep='--')

'''
Если в функцию ord передать не один символ а строку то выведится ошибка:
TypeError: ord() expected a character, but string of length 3 found
'''

'''
Функция chr обратна функции ord, она выводит
символ из цифры под которым он находится
'''

numA = chr(65)
numB = chr(66)
numC = chr(67)
print(numA, numB, numC, sep='--')