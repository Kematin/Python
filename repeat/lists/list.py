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

    animals.clear()
    print(animals) # []

methods_list()
