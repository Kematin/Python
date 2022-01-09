from random import *
from sys import *

check = input('Добро пожаловать, чтобы войти в напишите "Войти"\n*Если данных нет введите "Регистрация"\n')


if check.lower() == 'регистрация':
	def registration():
		login = input('Создайте свой логин: ')
		synced = open('занятые логины.txt', 'r') # открытие файла с занятыми логинами
		syn = synced.read()

		while login in syn:
			print('Данный логин занят') # цикл на определения занят логин или нет
			login = input('Введите другой желаемый логин ')
		synced.close()

		synced = open('занятые логины.txt', 'a') # запись логина в занятые логины
		synced.write(login)


		password = input('Создайте свой пароль: ')
		password_file = open('пароли.txt', 'w') # открытие текста с паролями
		password_file.write(password) # запись пароля
		password_file.close()

		print('Вы успешно зарегестрировались, теперь перезайдите в приложение')

	registration()

else:
	def check_system():
		login_file = open('занятые логины.txt', 'r')
		password_file = open('пароли.txt', 'r')

		login = input('\nВведите свой логин: ') # вход в систему
		password = input('Введите пароль: ')

		l_read = login_file.read()
		p_read = password_file.read()

		if login in l_read:         
			if p_read == password:
				return True             # проверка на вход
			else:
				return False
		else:
			return False

	check_files = check_system()

	while check_files != True: # цикл пока пользователь не введёт правильный пароль или логин
		print('Введён неверный пароль или логин, рекомендуеция пройти вход ещё раз или же зарегестрироваться')
		check_files = check_system()
	else:
		print('\nВы удачно вошли в систему\n')


#РЕЖИМ ШИФРОВАНИЕ СПОСОБОМ ЦЕЗАРЯ

def shifr():
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



#РЕЖИМ ВИСЕЛИЦА (УГАДАЙКА СЛОВ)



def viselica():
	word_list = ['Картошка', 'Окно', 'Пайтон', 'Удача', 'Красота', 'Програмирование', 'Лицо', 'Мышка',
	'Клавиатура', 'Малина', 'Велосипед', 'Машина', 'Ключ', 'Шарик']
	word = choice(word_list)


	# функция получения текущего состояния
	def display_hangman(tries):
		stages = [# финальное состояние: голова, торс, обе руки, обе ноги
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




#РЕЖИМ ЧИСЛОВАЯ УГАДАЙКА



def chislo_random():
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


#РЕЖИМ МАГИЧЕСКИЙ ШАР



def mag_shar():
	answer = ['Конечно', 'Абсолютно точно', 'Беспорная правда', 'Возможно', 'Знаки говорят - Да',
	'Будь уверен в этом', 'Абсолютная ложь', 'Никогда в жизни', 'Да', 'Нет', 'Ни за что', 'Наверное',
	'Лучше не торопиться', 'Спорный ответ', 'Даже не думай']

	print('Добро пожаловать дорогой пользователь, я магический шар и я могу предсказать что угодно')
	name = input('Начнём с твоего имени, как тебя зовут? ')
	print('Привет', name, end=' ')
	flag = input('хочешь ли ты начать получать предсказания? (введи + если да) ')

	while flag == '+':
		zap = input('Какой же вопрос ты хочешь задать?\n')
		print(choice(answer))
		flag = input('\nХочешь продолжить? (введи + если да) ')
	else:
		print('\n\nВозможно мы ещё встретимся...')




#РЕЖИМ ГЕНЕРАТОР ПАРОЛЕЙ

def paroli():
	nums = '0123456789'
	lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
	uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	punctuation = '!#$%&*+-=?@^_'
	chars = ''

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


#КАМЕНЬ НОЖНИЦЫ БУМАГА

def knb():
	agree = 'д'

	def knb_play():
		guesses = print('Для начала выберете один из предметов\n')
		gamelst = ['камень', 'бумага', 'ножницы']
		print(*gamelst, sep='\n')
		guesses = input('\n')
		gues_pk = choice(gamelst)


		def is_valid():
			for i in gamelst:
				if i == gamelst[2] and guesses.lower() != i:
					return False
					break
				if guesses.lower() != i:
					continue
				else:
					return True

		while is_valid() == False:
			guesses = input('\nВы ввели неверный предмет\n')
			is_valid()

		while True:
			if gues_pk == gamelst[1] and guesses.lower() == 'ножницы':
				print('\nТы выйграл, поздравляю! У меня была бумага')
				break

			elif gues_pk == gamelst[2] and guesses.lower() == 'камень':
				print('\nТы выйграл, поздравляю! У меня были ножницы')
				break

			elif gues_pk == gamelst[0] and guesses.lower() == 'бумага':
				print('\nТы выйграл, поздравляю! У меня был камень')
				break

			elif guesses.lower() == gues_pk:
				print('\nНичья, у меня была(ыл)', gues_pk)
				break

			else:
				print('\nТы проиграл, но может ещё повезёт! У меня была(ыл)', gues_pk)
				break

	while agree == 'д':
		knb_play()
		print('\nХотите сыграть ещё раз?(д - да, н - нет)\n')
		agree  = input()


def tic_tac_toe():
	tic_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	guess_lst_user = []
	guess_lst_pk = []
	tic_draw_X = [
				'''
				  |   |
		      ----|---|----
				  |   |
			  ----|---|----
				  |   |
				'''
	]
	guess = input('Введите клетку заполнения (от 1 до 9)\n')

	def is_valid():
		if guess.isdigit() == False:
			return False
		else:
			if len(guess) > 1:
				return False
			else:
				if guess in guess_lst_user:
					return False
				else:
					return True

	while is_valid() == False:
		guess = input('Вы ввели неправильное значение (либо вы уже вводили это число)\n')
		is_valid()
	guess_lst_user.append(guess)

	tic_list.remove(guess)
	pk_random = choice(tic_list)
	guess_lst_pk.append(pk_random)
	tic_list.remove(pk_random)






game_list = ['Шифровка способом Цезаря - 1', 'Виселица - 2', 
'Числовая угадайка - 3', 'Магический шар - 4', 'Генератор паролей - 5', 'Камень ножницы бумага - 6']


print('Сейчас доступны режимы:')
print(*[i for i in game_list], sep='\n')





# цикл проверки и выбора пользователя
agree = 'д'
while agree == 'д':
	guesses = input('\nВыберите цифру (или полное название) под нужным вам режимом\n')

	while guesses not in game_list and guesses not in '123456':
		guesses = input('Вы ввели не существующий на данный момент режим\nНапишите цифру под нужным вам режимом\n')

	else:
		if guesses == '1' or guesses.lower() == 'шифровка способом цезаря':
			print('\nШифровка способом цезаря - самый первый способ шифрования, не рекомендуеца шифровать важные сообщение, т.к. данный шифр легко взломать\n')
			shifr()
		elif guesses == '2' or guesses.lower() == 'виселица':
			print('\nВиселица - или же угадайка слов, игра в который загадывается слово и ты должен угадать его по буквам за определённое количество попыток, не угадал - проиграл!\n')
			viselica()
		elif guesses == '3' or guesses.lower() == 'числовая угадайка':
			print('\nЧисловая угадайка - игра в который ты загадываешь до какого числа будет загадана цифра, и ты с помощью подсказок должен угадать это число\n')
			chislo_random()
		elif guesses == '4' or guesses.lower() == 'магический шар':
			print('\nУтилита магический шар - простая программа в который вы задоёте вопрос на который можно ответить да или нет, и "Магический шар" случайно отвечает на него\n')
			mag_shar()
		elif guesses == '5' or guesses.lower() == 'генератор паролей':
			print('\nУтилита генератор паролей - прогрмма которое генерирует тебе пароль из твоих предпочтений\n')
			paroli()
		elif guesses == '6' or guesse.lower() == 'камень ножницы бумага':
			print('\nКамень, ножницы, бумага - известная игра, в которой 2 игрока выбирают камень, ножницы или бумагу\n(камень бьёт ножницы, бумага бьёт камень, а ножницы бьют бумагу)\n')
			knb()

	agree = input('\nХотите ли вы ещё опробовать другие программы? (д - да н - нет) \n')

else:
	print('До скорого дня, дорогой пользователь!')


