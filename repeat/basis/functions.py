'''
def name_function(argument_1, argument_2, etc):
    action
'''

def say_hi():
    print('Hello')

def say_bye():
    print('Good bye')


say_hi()
say_bye()



# create say_hello
def say_hello(name):
    print(f'Hello {name}!')

name = 'Tom'
# say_hello() error (missed argument)
say_hello(name) # call say_hello



# local functions

def main():
    
    def hello():
        print('Hello world!')

    def bye():
        print('Bye world!')

    hello()
    bye()

main()
# if we try to call local functions we except error
# hello() will except error (local function)


def f(x):
    y = x**2 + 5
    print(y)

x = 6
f(x)
# print(y) will except error (y - local variable)



# default values

def hello_people(name='Tom', age=18):
    print(f'Name: {name}')
    print(f'Age: {age}')

hello_people() # Name: Tom, Age: 18
hello_people('Bob') # Name: Bob, Age: 18
hello_people('Sam', 34) # Name: Sam, Age: 34



# Named arguments

hello_people(age=53, name='Mark') #Name: Mark, Age: 53

def people(name, /, *, company='Microsoft'):
    print(f'His name is {name} and he work in {company}')

# people('Tom', 'Apple') error: people take 1 argument, but 2 given *
# people(name='Tom', company='Apple') error: name positional argument /
people('Tom', company='Apple')


def sum_nums(*numbers):
    total = 0
    for n in numbers:
        total += n
    print(f'Sum = {total}')
    # print(sum(numbers))

sum_nums(1, 6, 3, 35, 3) # 9
sum_nums(4, 5) # 9




# return

def get_message():
    return 'Hello world'
print(get_message())
message = get_message()
print(f'message:\t{message}')

def f(x):
    y = x**2-53*2
    return y

def f_2(y):
    z = y % 3
    return z

def main(num=1):
    y = f(num)
    z = f_2(y)
    print(f'{x=}\n{y=}\n{z=}')

num_1 = 5
num_2 = 3
main(num_1)
main(num_2)


# Also at return we exit the function

def print_person(name, age):
    if age > 100 or age < 0:
        print(f'Invalid age for {name}')
        return
    print(f'Name: {name}\nAge: {age}')

first_person = 'Mark', 42
second_person = 'Bob', -100

print_person(*first_person)
print_person(*second_person)
