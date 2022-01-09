from random import *
nums = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print('Добро пожаловать в генератор паролей! Перед созданием паролей мне нужны ваши предпочтения')
kol = int(input('Сколько паролей вам нужно?\n'))
leng = int(input('\nКакая длина должна быть у пароля?\n'))
flag_nums = input('\nНужны ли цифры от 0 до 9 (введи + если да)\n')
flag_ll = input('\nНужны ли прописные буквы? (введи + если да)\n')
flag_ul = input('\nНужны ли строчные буквы? (введи + если да)\n')
flag_pun = input('\nНужны ли символы - !#$%&*+-=?@^_ (введи + если да)\n')

if flag_nums == '+':
	chars += nums
if flag_ll == '+':
	chars += lowercase_letters
if flag_ul == '+':
	chars += uppercase_letters
if flag_pun == '+':
	chars += punctuation


def gen_paroli(leng, letter):
	password = ''
	for i in range(leng):
		password += choice(letter)
	return password

print('\nВот ваш(и) пароль(и)')
for _ in range(kol):
	print(gen_paroli(leng, chars))
		