'''
class child class(parent class):
    methods and atributes
'''
class A():
    x = 5

class B(A):
    def set_x(self):
        self.x = 8

def test():
    first_x = A()
    print(first_x.x)

    second_x = B()
    print(second_x.x) # = first_x

    second_x.set_x()
    print(second_x.x) # = 8



# Overriding the functionality of a base class

class Person():
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    def set_age(self, age):
        if 1 < age < 120:
            self.__age = age
        else:
            print('Uncorrect age')

    @property
    def get_name(self):
        return self.__name

    def display_info(self):
        print(f'Name: {self.__name}\nAge: {self.__age}')

    def nothing(self):
        print(f'{self.__name} does nothing')


class Employee(Person):
    def __init__(self, name, company: str, id_work):
        super().__init__(name) # change atribute from parent class
        self.company = company
        self.__id = id_work

    def display_info(self):
        super().display_info() # use method from parent class 
        print(f'Work in {self.company}\nId: {self.__id}')


def people():
    tom = Person('Tom')
    tom.set_age(24)
    tom.display_info()

def employee():
    mark = Employee('Mark', 'Microsoft', 4525124)
    mark.set_age(27)
    mark.display_info()



# Checking the object type
# isinstance(object, type)

class Student(Person):

    def study(self):
        name = self.get_name
        print(f'{name} study')

class Work(Person):

    def work(self):
        name = self.get_name
        print(f'{name} working')


def act(man):
    if isinstance(man, Work):
        man.work()
    elif isinstance(man, Student):
        man.study()
    elif isinstance(man, Person):
        man.nothing()

def peoples():
    tom = Student('Tom')
    bob = Person('Bob')
    sam = Work('Sam')
    for person in (tom, bob, sam):
        act(person)

peoples()
