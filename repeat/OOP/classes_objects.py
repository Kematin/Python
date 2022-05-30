'''
class name():
    method()
    atribute = *

object = name()
'''

class Person():

    def say_message(self, message): # method 1
        print(message)

    hello = lambda self: print('hello') # method 2


def person():
    mark = Person() # object
    mark.say_message('Hello my friend')
    mark.hello()


'''
accessing methods and attributes
self.atribute
self.method
'''

class Calculate():
    n, m = int, int

    def sum_nums(self):
        return (self.n + self.m)

    def sub_nums(self):
        return (self.n - self.m)

    def calc(self):
        print(f'{self.n} + {self.m} = {self.sum_nums()}')
        print(f'{self.n} - {self.m} = {self.sub_nums()}')

def Calc():
    calculate = Calculate()

    calculate.n, calculate.m = 5, 3
    calculate.calc()

    calculate.n, calculate.m = 9, 134
    calculate.calc()



# Constructors

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Name: {self.name}\nAge: {self.age}')


def constructors():
    tom = Person('Tom', 27)
    tom.say_hello()

    bob = tom
    bob.name = 'Bob'
    bob.say_hello()

constructors()
