#range
'''
range с 1 аргументом
for i in range(5):
    print('A')
выведится 5 раз A

range с 2 аргументами
for i in range(4, 10):
    print(i)
выведится 6 цифр от 4 до 10 (4 5 6 7 8 9)

range c 3 аргументами
for i in range(1, 10, 2):
    print(i)
будет выводится всё числа от 1 до 10 через 2 шага (1 3 5 7 9)
'''
for i in range(5):
    print('A')
for i in range(4, 10):
    print(i)
for i in range(1, 10, 2):
    print(i)
'''
Отрицательный шаг генерации
for i in range(1, 10, -1):
    print(i)
print('Взлетаем!!!')
'''

for i in range(9, 1, -1):
    print(i, '--')
'''
первый параметр – это старт последовательности (включительно);
второй параметр – это стоп последовательности (не включительно);
третий параметр – это величина шага.
'''