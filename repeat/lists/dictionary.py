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


    #check key in dictionary
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
    phone_bill = users.get('Bill', 'Undefined')
    phone_larry = users.get('Larry', 'Undefined')
    print(f'Bill: {phone_bill}\nLarry: {phone_larry}')



def for_in_dict():
    elements = {
        'Name': 'Bob',
        'Phone': '+6953135',
        'Company': 'Microsoft',
    }
    for key, value in elements.items():
        print(f'{key}: {value}') 

    for key in elements.keys():
        print(key)

    for value in elements.values():
        print(value)
    

def complex_dict():
    users = {

        'Tom': {
            'email': 'tom_work@gmail.com',
            'age': 34
        },

        'Bob': {
            'email': 'bob@gmail.com',
            'age': 13
        }

    }
    old_email = users['Bob']['email']
    new_email = 'work_bob@rumbler.com'
    users['Bob']['email'] = new_email
    print(users['Bob']) # {email: work_bob@rumbler.com, ...}

    for user, info in users.items():
        print(user)
        for i in info:
            print(f'{i}: {info[i]}')
        print('\n')


def del_from_dict():
    values = {
        1: 53.23,
        2: True,
        3: 'Name'
    }
    check_keys = 2, '3'
    for key in check_keys:
        if key in values:
            del values[key]
            print(f'Key: {key} was removed from dict')
        else:
            print(f'Key: {key} not in dict')

    values[4] = 1000
    value_1 = values.pop(1, 'Undefined')
    value_2 = values.pop(5, 'Undefined')
    print(f'value 1 was delete from dict and = {value_1}',
            f'\nvalue 2 was delete from dict and = {value_2}')
    # print(values[1]) KeyError

    values_2 = values.copy() # {3: Name, 4: 1000}
    values_2.clear() # {}
    values_2[1] = 5000

    values.update(values_2)
    print(values) # {3: Name, 4: 1000, 1: 5000}



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


if __name__ == '__main__':
    complex_dict()
