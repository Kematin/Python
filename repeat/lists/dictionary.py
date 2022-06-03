'''
dictionary = {
    key_1: value_1,
    key_2: value_2,
    ...
}
print(dictionary[some_key]) # some value
'''

def dictionary():
    # objects = dict()
    objects = {
        1: 'Name',
        '2': True,
        3.34: 13.53
    }
    # print(objects[2]) KeyError
    print(objects[3.34]) # 13.53


    # We can also do a conversion from tuple and list
    users_list = [
        ['Mark', '+951358953'],
        ['Tom', '+1111111111'],
        ['Bill', '+63185363'],
    ]
    users = dict(users_list)
    print(users) # {'Mark': '+951358953', ...}

    check_keys = 'Tom', 'Bob'
    for key in check_keys:
        if key in users:
            phone = users[key]
            print(phone)
        else:
            print(f'Key: {key} not in dictionary')


    users['Bill'] = '+22222222222'
    print(users['Bill']) # +222222222

    # append new value in dictionary
    users['Bob'] = '+333333333'
    print(users['Bob'])

    # get(key, default)
    

dictionary()


class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 1

    def set_age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print('Error')

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.__age}\n'


def for_person():
    users = {
        1: ['Tom', 33],
        2: ['Bill', 23],
        3: ['Mark', 52],
    }
    for key in users:
        person = Person(users[key][0])
        person.set_age(users[key][1])
        print(person)
        
