#Строки



'''
s = 'abcdefghij'
Программный код	
s[2:5]	cde	строка состоящая из символов с индексами 2, 3, 4
s[:5]	abcde	первые пять символов строки
s[5:]	fghij	строка состоящая из символов с индексами от 5 до конца
s[-2:]	ij	последние два символа строки
s[:]	abcdefghij	вся строка целиком
s[1:7:2]	bdf	строка состоящая из каждого второго символа с индексами от 1 до 6
s[::-1]	jihgfedcba	строка в обратном порядке, так как шаг отрицательный
'''



'''
Если мы хотим поменять какой-либо символ строки s, 
мы должны создать новую строку. 
Следующий код использует срезы и решает поставленную задачу:

s = s[:4] + 'X' + s[5:]
Мы создаем два среза: от начала строки до 3 символа и с 5 символа 
по конец строки, а между ними вставляем нужный нам символ, который встанет на 4 позицию.
'''


'''
Метод capitalize() возвращает копию строки s, в которой первый 
символ имеет верхний регистр, а все остальные символы имеют нижний регистр.
'''


'''
Метод swapcase() возвращает копию строки s, в которой все символы, 
имеющие верхний регистр, преобразуются в символы нижнего регистра и наоборот.
'''


'''
Метод title() возвращает копию строки s, в которой первый символ каждого 
слова переводится в верхний регистр.
'''






s = 'bAALLALAA'
print(s.capitalize())
#Вывод Baallalaa



s = 'KAAAlaaa'
print(s.swapcase())
#Вывод kaaaLAAA


s = 'the sun also rises'
print(s.title())
#Вывод My Names Rafael


s = 'BAKA'
print(s.lower())
#Вывод baka


s = 'baka'
print(s.upper())
#Вывод BAKA