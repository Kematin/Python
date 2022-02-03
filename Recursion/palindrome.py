#Palindrome 
import math
def check_palindrome(word, i):
    if i + 1 == math.floor(len(word.lower()) / 2): return True
    k = int('-' + str(i + 1))
    elif word.lower()[i] == word.lower()[k]:
        i += 1
        check_palindrome(word, i)
    else: return False

word = 'Доход'

if check_palindrome(word, 0):
    print(f'Слово "{word}" палиндром')
else: print(f'Слово "{word}" не палиндром')

