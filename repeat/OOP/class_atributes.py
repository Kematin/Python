class Person:
    type = 'Person'
    def __init__(self, name):
        self.name = name


def types():
    tom = Person('Tom')
    bob = Person('Bob')
    print(tom.type) # Person
    print(bob.type) # Person

    # change atribute of class
    Person.type = 'Class Person'

    print(tom.type) # Class Person
    print(bob.type) # Class Person







    


'''
Class attributes can be used for situations where 
we need to define some common data for all objects
'''

class Person:
    default_name = None

    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = Person.default_name


def types_2():
    mark = Person('Mark')
    tony = Person('')

    print(mark.name) # Mark
    print(tony.name) # None









class Person:
    name = 'Undefined'

    print_name = lambda self: print(self.name)

def types_3():
    bob = Person()
    mark = Person()
    bob.print_name() # Undefined
    mark.print_name() # Undefined

    Person.name = 'Some person'
    bob.print_name() # Some person
    mark.print_name() # Some person

    bob.name = 'Bob'
    bob.print_name() # Bob
    mark.print_name() # Some person









# Static method
class Person:
    pass
