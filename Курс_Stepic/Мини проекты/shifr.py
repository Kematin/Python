from sys import *
language = input('Язык (ru, en): ')

def caesar(alphabet):
	text = input("Текст: ")
	shift = ii("Отступ: ")



	def get_char(char, alphabet_, shift_):
		if char.isalpha():
			i = 0
			if char.isupper():
				i = 1
			return alphabet_[i][(alphabet_[i].index(char) + shift_) % len(alphabet_[0])]
		return char


	shifted = "".join([get_char(char, alphabet, shift) for char in text])
	print(shifted)


def english_alphabet():
	return "".join([chr(char) for char in range(ord("a"), ord("z") + 1)])

def russian_alphabet():
	return "".join([chr(char) for char in range(ord("а"), ord("я") + 1)])


def ii(message=""):
	return int(input(message))
 
while language != 'ru' and language != 'en':
	print('Введён неверный язык')
	language = input('Введите язык: ')
else:
	if language == 'ru':
		caesar([russian_alphabet(), russian_alphabet().upper()])
	elif language == 'en':
		caesar([english_alphabet(), english_alphabet().upper()])

