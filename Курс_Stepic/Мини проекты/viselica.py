from random import *
word_list = ['Картошка', 'Окно', 'Пайтон', 'Удача', 'Красота', 'Програмирование', 'Лицо', 'Мышка',
'Клавиатура', 'Малина', 'Велосипед', 'Машина', 'Ключ', 'Шарик']
word = choice(word_list)


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     | |
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
	guessed_letters = []              # список уже названных букв
	letters = ''
	tries = 6     					   # попытки
	win = 0

	print('Вот твоё начальное состояние, со временем оно будет ухудшаться', 
		display_hangman(tries), 
		'И как только ты полностью будешь на виселице ты проиграешь!', 
		sep='\n')

	print(*['_' for i in range(len(word))], sep='\n')

	while True:
		letter = input('Введите букву ')

		while letter in guessed_letters:
			letter = input('Вы уже вводили эту букву, склерозник\nВведите букву ')
			while letter.isalpha() == False or len(letter) != 1:
				print('Нужно вводить лишь 1 букву и всё! Это так сложно? ')
				letter = input('Введите букву ')
		guessed_letters.append(letter)




		if letter in word.lower():
			for i in word.lower():
				if i == letter:
					win += 1

		if letter not in word.lower():
			tries -= 1
			print('Веденна неверная буква ваще текущее состояние', display_hangman(tries))
		elif letter in word.lower() and letter not in letters:
			letters += letter


		for i in word.lower():
			if i in letters:
				print(i)
			else:
				print('_')



		if tries < 1:
			print('Вы проиграли! Ну ничего может ещё повезёт, загаданное слово -', word)
			break
		elif win == len(word):
			print('Вы попедили, поздравляем! ')
			break

agree = '+'
print('Привет, давай начнём играть в виселицу!')
while agree == '+':
	play(word)
	agree = input('\nХочешь продолжить играть? (введи + если да) ')
	word_list.remove(word)
	word = choice(word_list)
else:
	print('Спасибо что сыграли в мою игру, удачи!')