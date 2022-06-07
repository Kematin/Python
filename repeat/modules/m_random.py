import random

def functions_random():
    number = random.randint(3, 100) # random number in range 3, 100 (int)
    print(number)

    number = random.random() # random number in range 0, 1 (float)
    print(number)

    number = random.randrange(1, 10, 2) # random number in range 1, 3, 5, ... (float)
    print(number)

    nums = list(range(1, 10))
    random.shuffle(nums) # shuffles the list
    print(nums)

    number = random.choice(nums) # take random value from list
    print(number)


functions_random()
