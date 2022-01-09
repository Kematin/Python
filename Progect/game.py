#Игра
import random
import time
from colorama import Fore, Back, Style
from colorama import init

hard = input("Выберите уровень сложности: Easy, Normal, Hard, Excpert: ")
words = ['game', 'magic', 'itachi', 'windows', 'good', 'morning', 'gon']
word = random.choice(words)
time.sleep(0.5)
guesses = ''
turns = [15, 12, 9, 7]
wrong = 0







if hard == "Easy":
	print(Back.GREEN)
	print(Fore.BLACK)

	print('{game:^162}'.format(game = "Ну что-ж начнём игру"))
	while turns[0] > 0:
		wrong = 0

		for char in word:
			if char in guesses:
				print (char)
			else:
				print(Back.BLACK)
				print(Fore.YELLOW)
				print ("?")
				wrong += 1

		print("\n")

		if wrong == 0:
			print(Back.YELLOW)
			print(Fore.BLACK)
			print ("{won:^162}".format(won = "Ты выйграл :D"))

			break

		print

		guess = ''
		if len(guess) < 1:
			print(Back.BLACK)
			print(Fore.BLUE)
			guess = input("Выбери букву которую хочешь вставить: ")[0]

		guesses += guess

		if guess not in word:
			turns[0] -= 1
			print(Fore.RED)
			print ("Неверно")
			print(Fore.BLUE)
			print ('У тебя осталось ' + str(turns[0]) + ' шагов!')

			if turns[0] == 0:
				print(Back.RED)
				print(Fore.BLACK)
				print("{lose:^162}".format(lose = "ТЫ ПРОИГРАЛ"))









elif hard == "Normal":
	print(Back.GREEN)
	print(Fore.BLACK)

	print('{game:^162}'.format(game = "Ну что-ж начнём игру"))
	while turns[1] > 0:
		wrong = 0

		for char in word:
			if char in guesses:
				print (char)
			else:
				print(Back.BLACK)
				print(Fore.YELLOW)
				print ("?")
				wrong += 1

		print("\n")

		if wrong == 0:
			print(Back.YELLOW)
			print(Fore.BLACK)
			print ("{won:^162}".format(won = "Ты выйграл :D"))

			break

		print

		guess = ''
		if len(guess) < 1:
			print(Back.BLACK)
			print(Fore.BLUE)
			guess = input("Выбери букву которую хочешь вставить: ")[0]

		guesses += guess

		if guess not in word:
			turns[1] -= 1
			print(Fore.RED)
			print ("Неверно")
			print(Fore.BLUE)
			print ('У тебя осталось ' + str(turns[1]) + ' шагов!')

			if turns[1] == 0:
				print(Back.RED)
				print(Fore.BLACK)
				print("{lose:^162}".format(lose = "ТЫ ПРОИГРАЛ"))








elif hard == "Hard":
	print(Back.GREEN)
	print(Fore.BLACK)

	print('{game:^162}'.format(game = "Ну что-ж начнём игру"))
	while turns[2] > 0:
		wrong = 0

		for char in word:
			if char in guesses:
				print (char)
			else:
				print(Back.BLACK)
				print(Fore.YELLOW)
				print ("?")
				wrong += 1

		print("\n")

		if wrong == 0:
			print(Back.YELLOW)
			print(Fore.BLACK)
			print ("{won:^162}".format(won = "Ты выйграл :D"))

			break

		print

		guess = ''
		if len(guess) < 1:
			print(Back.BLACK)
			print(Fore.BLUE)
			guess = input("Выбери букву которую хочешь вставить: ")[0]

		guesses += guess

		if guess not in word:
			turns[2] -= 1
			print(Fore.RED)
			print ("Неверно")
			print(Fore.BLUE)
			print ('У тебя осталось ' + str(turns[2]) + ' шагов!')

			if turns[2] == 0:
				print(Back.RED)
				print(Fore.BLACK)
				print("{lose:^162}".format(lose = "ТЫ ПРОИГРАЛ"))
			













elif hard == "Excpert":
	print(Back.GREEN)
	print(Fore.BLACK)

	print('{game:^162}'.format(game = "Ну что-ж начнём игру"))
	while turns[3] > 0:
		wrong = 0

		for char in word:
			if char in guesses:
				print (char)
			else:
				print(Back.BLACK)
				print(Fore.YELLOW)
				print ("?")
				wrong += 1

		print("\n")

		if wrong == 0:
			print(Back.YELLOW)
			print(Fore.BLACK)
			print ("{won:^162}".format(won = "Ты выйграл :D"))

			break

		print

		guess = ''
		if len(guess) < 1:
			print(Back.BLACK)
			print(Fore.BLUE)
			guess = input("Выбери букву которую хочешь вставить: ")[0]

		guesses += guess

		if guess not in word:
			turns[3] -= 1
			print(Fore.RED)
			print ("Неверно")
			print(Fore.BLUE)
			print ('У тебя осталось ' + str(turns[3]) + ' шагов!')

			if turns[3] == 0:
				print(Back.RED)
				print(Fore.BLACK)
				print("{lose:^162}".format(lose = "ТЫ ПРОИГРАЛ"))





else:
	print("Я не думаю что ты выбрал нужный уровень сложности ~_~")
