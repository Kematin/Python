from random import *


print('Добро пожаловать в числовую угадайку')
ran = int(input('Укажите до какой границы будет задано число: '))
num = randint(1, ran)

def is_valid(answer):
    if answer.isdigit():
        answer = int(answer)
        if 1 <= answer <= ran:
            return True
        else:
            return False
    else:
        return False




answer = input('Введите число: ')
count = 0

while answer != str(num):
	if is_valid(answer) == False:
		print('А может быть все-таки введем целое число от 1 до', str(ran) + '?')
		answer = input()
		continue
	answer = int(answer)


	if answer < num:
		print('Ваше число меньше загаданного, попробуйте еще разок')
		answer = input('\nВведите число ещё разок: ')
	else:
		print('Ваше число больше загаданного, попробуйте еще разок')
		answer = input('\nВведите число ещё разок: ')
	count += 1

else:
	print('\nВы угадали, поздравляем!')



cont = input('\nХотите сыграть ещё раз? (введите + если да) ')

while cont == '+':
	answer = input('Введите число: ')

	while answer != str(num):
		if is_valid(answer) == False:
			print('А может быть все-таки введем целое число от 1 до', str(ran) + '?')
			answer = input()
			continue
		answer = int(answer)


		if answer < num:
			print('Ваше число меньше загаданного, попробуйте еще разок')
			answer = input('\nВведите число ещё разок: ')
		else:
			print('Ваше число больше загаданного, попробуйте еще разок')
			answer = input('\nВведите число ещё разок: ')
		count += 1

	else:
		print('\nВы угадали, поздравляем!')

	cont = input('\nХотите сыграть ещё раз (введите + если да)')
else:
	print('\n' + 'Спасибо, что играли в числовую угадайку. Всего на угадание чисел вы потратили', count, 'попыток.')





