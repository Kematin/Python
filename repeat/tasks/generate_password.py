from random import choice
import string

letters = list(string.ascii_letters)
digits = [str(i) for i in range(10)]
punctuation = list(string.punctuation)

def get_part(part, how_much):
    pass

def main():
    add_letters = input('Add letters in password? (+ - yes)')
    add_nums = input('Add nums in password? (+ - yes)')
    add_punct = input('Add punctuation in password? (+ - yes)')
    

def fast_generate_for_me():
    all_in_one = letters + digits + punctuation
    without_punctuation = letters + digits

    result_1 = ''.join(choice(all_in_one) for _ in range(40))
    result_2 = ''.join(choice(without_punctuation) for _ in range(40))

    print(f'{result_1}\n{result_2}')

if __name__ == '__main__':
    fast_generate_for_me()
