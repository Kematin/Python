# Withoit encapsulation

class Person():
    def __init__(self, name):
        self.name = name
        self.age = 1

    def say_hello(self):
        print(f'Name: {self.name}\nAge: {self.age}')


def person():
    bob = Person('Bob')
    bob.name = 'Mark' # change atribute name
    bob.age = 24 # change atribute age
    bob.say_hello()


# With encapsulation

class PersonNew():
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    @property # getter
    def age(self): 
        return self.__age

    @age.setter # setter
    def age(self, age):  
        if 1 < age < 120:
            self.__age = age
        else:
            print('Uncorrect age')

    def get_name(self):
        return self.__name
   
    def display_info(self):
        print(f'Name: {self.__name}\nAge: {self.__age}')

def new_person():
    tom = PersonNew('Tom')

    tom.age = 53
    print(tom.age) # 53
    tom.age = -34 # Uncorrect age

    tom.display_info() # Name: Tom, Age: 53
    # also we cant change the name in the class (no setter)
    tom.name = 'Bob'
    print(tom.get_name()) # Tom

new_person()
