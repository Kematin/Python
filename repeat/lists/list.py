# list

def create_list():
    nums = [0, 1, 2, 3, 4, 5]
    people = ['Tom', 'Bob', 'Mark']
    is_valid = [True, False]

    all_in_one = ['Tim', 54, 14.32, True]
    some_list = list()
    # better than: some_list = []

    message = 'Hello'
    message_list = list(message)
    print(message_list) # ['H', 'e', 'l', 'l', 'o']

    nums_list = list(range(2, 11, 2)) # [2, 4, 6, 8, 10]
    print(nums_list)

    nums_list = [5]
    print(nums_list * 5) # [5, 5, 5, 5, 5]


def index_list():
    people = ['Tom', 'Sam', 'Mark']
    print(people[2]) # Mark (index start from 0: Tom)
    print(people[-2]) # Sam (index start from -1: Mark)

    people[0] = 'Kavin'
    print(people[0]) # Kavin

    kavin, sam, mark = people
    print(kavin, sam, mark + 'Me') # Kavin, Sam, MarkMe

    # Overseeing the elements
    nums = [10, 50, 20]
    for num in nums:
        print(num)

    for i in range(1, len(nums) + 1):
        print(nums[-i]) # 20, 50, 10


def methods_list():
    animals = ['elephant', 'dog']
    animals.append('cat')
    print(animals) # elephant, dog, cat

    animals.insert(1, 'tiger')
    print(animals) # elephant, tiger, dog, cat

    alphafit = ['a', 'b', 'c']
    alphafit.extend('defg')
    print(alphafit) # a, b, c, d, e, f, g

    item = 'dog'
    animals.remove(item)
    print(animals) # elephant, tiger, cat

    index_of_cat = animals.index('cat')
    print(index_of_cat) # 2

    animals.pop(index_of_cat)
    print(animals) # elephant, tiger

    letters = ['a', 'b', 'c', 'd', 'a', 'a', 'b']
    how_much_a = letters.count('a')
    print(how_much_a) # 3

    letters.sort()
    print(letters) # a, a, a, b, b, c, d

    letters.reverse()
    print(letters) # d, c, b, b, a, a, a

    del letters[4:]
    print(letters) # d, c, b, b

    animals.clear()
    print(animals) # []


def why_copy_better():
    a = [1, 2, 3]
    b = a

    b.append(4)
    print(a) # should be 1, 2, 3, but print 1, 2, 3, 4
    a.pop(0)
    print(b) # should be 1, 2, 3, 4 but print 2, 3, 4


    a = [1, 2, 3]
    b = a.copy()

    b.append(4)
    print(a) # 1, 2, 3 
    print(b) # 1, 2, 3, 4

    a.pop(0)
    print(a) # 2, 3
    print(b) # 1, 2, 3, 4


def functions_for_list():
    numbers = [4, 2, 5, 1]

    len_of_list = len(numbers)
    print(len_of_list) # 4

    sorted_numbers = sorted(numbers)
    print(sorted_numbers) # 1, 2, 4, 5

    min_element = min(numbers)
    print(min_element) # 1

    max_element = max(numbers)
    print(max_element) # 5


def is_element():
    people = ['Tom', 'Alice', 'Mark']
    try:
        people.remove('Alice')
        print(people)

        people.remove('Bob')
        print(people)
    except ValueError:
        print('Element not in list')

    print('End programm')



'''
list[start:end:step]
letters = [[0, 1, 2], [4, 5, 6]]
five = letters[1][1]
'''

def slices_lists():
    numbers = list(i for i in range(1, 11))
    odd_numbers = numbers[::2]
    even_numbers = numbers[1::2]
    print(f'{odd_numbers}\n{even_numbers}') # 1, 3, 5, 7, 8 \n 2, 4, 6, 8, 10

    peoples = [
        ['Tom', 26],
        ['Bob', 43],
        ['Mark', 14],
    ]
    print(*peoples[1]) # Bob 43
    print(peoples[2][0]) # Mark

    for people in peoples:
        name, age = people
        print(f'Name: {name}\nAge: {age}')

    peoples[-1].append('+7843245932')
    print(peoples[-1]) # Mark, 14, +7843245932

slices_lists()
