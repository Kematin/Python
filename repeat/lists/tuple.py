'''
list = []
tuple = ()
unlike list, tuple cannot be changed
'''

def tuple():
    tom = 'Tom', 24
    print(tom) # ('Tom', 24)

    mark = 'Mark', 14, 'Google'
    print(len(mark)) # 3
    print(f'Age: {mark[1]}')
    # mark[0] = 'Tim' TypeError
    print(mark[1:]) # (14, 'Google')

    def get_info_person():
        name = 'Bob'
        age = 24
        company = 'Microsoft'

        return name, age, company # we return tuple (name, age, company)

    def print_about_person(name, age, company):
        print(f'Name: {name}\nAge: {age}\nCompany: {company}')

    bob = get_info_person() # ('Bob', 24, 'Microsoft')
    tom = ('Tom', 34)

    print_about_person(*bob)
    print_about_person(*tom, 'Google')

    items = 'Apple', 'Knife', 'Book'

    for item in items:
        print(item)

tuple()
