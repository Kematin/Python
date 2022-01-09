#Калькулятор V2
from colorama import Fore, Back, Style
from colorama import init

print(Back.WHITE)
print("Программа запущенна" + '\n\n')

init()
print(Fore.BLACK)
print(Back.GREEN)



a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число (если оно не нужно введите 0): "))
if a or b or c == str:
	raise ValueError("Неправильное значение для a, b или c")
#except ValueError:
	#print("Неправильное значение для a, b или c")

print(Back.YELLOW)
what = input("Введите знак вычисления: ")
what2 = input("Введите второй знак вычисления (если он не нужен введите 0): ")


print(Back.MAGENTA)



if what == "+" and what2 == "0" or c == "0":
	d = a + b
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "0" or c == "0":
	d = a - b
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "0" or c == "0" and b != "0" or a != "0":
	d = a / b
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "0" or c == "0":
	d = a * b
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "0" or c == "0":
	d = a ** b
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "0" or c == "0":
	d = a // b
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "0" or c == "0":
	d = a % b
	print('Ответ ' + str(d) + "\n\n")




elif what == "+" and what2 == "+":
	d = a + b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "*":
	d = a + b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "/":
	d = a + b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "-":
	d = a + b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "//":
	d = a + b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "%":
	d = a + b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "**" or what2 == "^":
	d = a + b ** c
	print('Ответ ' + str(d) + "\n\n")



elif what == "/" and what2 == "+":
	d = a / b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "+":
	d = a * b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "+":
	d = a - b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "+":
	d = a // b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "+":
	d = a % b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "+":
	d = a ** b + c
	print('Ответ ' + str(d) + "\n\n")



elif what == "+" and what2 == "-":
	d = a + b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "-":
	d = a ** b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "-":
	d = a / b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "-":
	d = a // b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "-":
	d = a % b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "-":
	d = a * b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "-":
	d = a - b - c
	print('Ответ ' + str(d) + "\n\n")


elif what == "//" and what2 == "//":
	d = a // b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "//":
	d = a - b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "//":
	d = a * b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "//":
	d = a / b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "//":
	d = a % b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "//":
	d = a + b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "//":
	d = a ** b // c
	print('Ответ ' + str(d) + "\n\n")


elif what == "**" or what == "^" and what2 == "**" or what2 == "^":
	d = a ** b ** c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "**" or what2 == "^":
	d = a + b ** c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "**" or what2 == "^":
	d = a - b ** c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "**" or what2 == "^":
	d = a // b ** c
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "**" or what2 == "^":
	d = a * b ** c
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "**" or what2 == "^":
	d = a / b ** c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "**" or what2 == "^":
	d = a % b ** c
	print('Ответ ' + str(d) + "\n\n")


elif what == "*" and what2 == "*":
	d = a * b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "*":
	d = a + b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "*":
	d = a - b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "*":
	d = a / b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "*":
	d = a // b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "*":
	d = a ** b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "*":
	d = a % b * c
	print('Ответ ' + str(d) + "\n\n")


elif what == "/" and what2 == "/":
	d = a / b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "/":
	d = a + b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "/":
	d = a - b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "/":
	d = a * b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "/":
	d = a // b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "/":
	d = a % b / c
	print('Ответ ' + str(d) + "\n\n")
elif what == "**" or what == "^" and what2 == "/":
	d = a ** b / c
	print("Ответ " + str(d) + "\n\n")




elif what == "*" and what2 == "%":
	d = a * b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "+" and what2 == "%":
	d = a + b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "%":
	d = a - b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "%":
	d = a / b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "%":
	d = a // b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "%":
	d = a ** b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "%":
	d = a % b % c
	print('Ответ ' + str(d) + "\n\n")



elif what == "-" and what2 == "*":
	d = a - b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "//":
	d = a - b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "/":
	d = a - b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "%":
	d = a - b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "+":
	d = a - b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "-" and what2 == "**" or what2 == "^":
	d = a - b ** c
	print('Ответ ' + str(d) + "\n\n")



elif what == "*" and what2 == "-":
	d = a * b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "//":
	d = a * b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "/":
	d = a * b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "%":
	d = a * b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "+":
	d = a * b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "*" and what2 == "**" or what2 == "^":
	d = a * b ** c
	print('Ответ ' + str(d) + "\n\n")



elif what == "/" and what2 == "*":
	d = a / b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "//":
	d = a / b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "-":
	d = a / b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "%":
	d = a / b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "+":
	d = a / b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "/" and what2 == "**" or what2 == "^":
	d = a / b ** c
	print('Ответ ' + str(d) + "\n\n")



elif what == "%" and what2 == "*":
	d = a % b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "//":
	d = a % b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "/":
	d = a % b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "-":
	d = a % b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "+":
	d = a % b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "%" and what2 == "**" or what2 == "^":
	d = a % b ** c
	print('Ответ ' + str(d) + "\n\n")



elif what == "//" and what2 == "*":
	d = a // b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "-":
	d = a // b - c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "/":
	d = a // b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "%":
	d = a // b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "+":
	d = a // b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "//" and what2 == "**" or what2 == "^":
	d = a // b ** c
	print('Ответ ' + str(d) + "\n\n")




elif what == "**" or what == "^" and what2 == "*":
	d = a ** b * c
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "//":
	d = a ** b // c
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "/":
	d = a ** b / c
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "%":
	d = a ** b % c
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "+":
	d = a ** b + c
	print('Ответ ' + str(d) + "\n\n")

elif what == "**" or what == "^" and what2 == "-":
	d = a ** b - c
	print('Ответ ' + str(d) + "\n\n")


else:
	print("Неизвестая операция")



print(Back.WHITE)
print("Программа завершенна (нажмите Enter для выхода)")
input()