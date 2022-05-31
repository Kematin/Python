# raise

def division_nums(a=1, b=1):
    result = a / b
    return result

def except_error():
    try:
        a = int(input('Num 1: '))
        b = int(input('Num 2: '))
        print(f'{a} / {b} = {division_nums(a, b)}')
        if b == 0:
            raise ExceptionError('Num 2 cant be equal to 0')
    except ValueError:
        print('Num need be equal to intenger')
    except ExceptionError as e:
        print(e)

    print('End programm')


class PersonExceptError(Exception):
    def __init__(self, age, min_age, max_age):
        self.age = age
        self.min_age = min_age
        self.max_age = max_age

    def __str__(self):
        return f'Uncorrect age: {self.age}\nAge must be in the range of {self.min_age}, {self.max_age}'

class Person:
    def __init__(self, age, name):
        self.name = name
        minage, maxage = 1, 100
        if minage < age < maxage:
            self.age = age
        else:
            raise PersonExceptError(age, minage, maxage)

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}'

def try_object():
    try:
        tom = Person(20, 'Tom')
        print(tom)

        bob = Person(-13, 'Bob')
        print(bob)
    except PersonExceptError as p:
        print(p)

try_object()
