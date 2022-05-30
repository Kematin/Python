'''
in the Python programming language implicitly have one common superclass, 
*object, and all classes inherit its methods by default.
'''
# __str__()

class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def set_age(self, age):
        if  100 < age < 0:
            print('Uncorect age')
        else:
            self.age = age

    def about_class(self):
        print(f'Name: {self.name}\nAge: {self.age}')

def default():
    tom = Person('Tom')
    tom.set_age(24)
    print(tom) # <__main__.Person object at 0x7f215956a190>

default()


class Person_2(Person):
    def __init__(self, name):
        super().__init__(name)
        self.age = 1

    def __str__(self):
        print(f'Name: {self.name}\nAge: {self.age}')


def change_str():
    bob = Person_2('Bob')
    bob.set_age(20)
    print(bob) # Name: Bob, Age: 20
    print(bob.abot_class) # Name: Bob, Age: 20

change_str()
