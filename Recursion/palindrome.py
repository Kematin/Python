#Palindrome 
import math
def check_palindrome(word, i):
    if i == math.floor(len(word.lower()) / 2): return True
    k = int('-' + str(i + 1))
    if word.lower()[i] != word.lower()[k]: return False
    else:
        i += 1
        check_palindrome(word, i)
        return True 

word = input('Введите слово\n')
check = check_palindrome(word, 0)

if check:
    print(f'Слово "{word}" палиндром')
else: print(f'Слово "{word}" не палиндром')

