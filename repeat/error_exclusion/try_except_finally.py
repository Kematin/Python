'''
2 type of error:
    syntax error
    runtime error

print('hello world' <- syntax error
print(int('Hello world')) <- runtime error (at compile time)

try handles runtime errors
'''

'''
try:
    instruction
except [Type of error]:
    insctruction
'''

def get_num():
    num = input('Write num: ')
    return int(num)

def except_value_error():
    try:
        num = get_num()
        print(f'Num in ^ 2 = {num**2}')
    except ValueError:
        print(f'Your input not number')

    print('End programm')


'''
optional block finally called in any case, 
more often used to work with files to release resources
'''

def calculate(div_1, div_2):
    num = div_2 / div_2
    return num

def except_zero_error():
    try:
        num_1 = int(input('Number 1: '))
        num_2 = int(input('Number 2: '))
        num = calculate(num_1, num_2)
        print(f'{num_1} / {num_2} = {num}')
    except ZeroDivisionError:
        print('num 2 cant to be 0!')
    finally:
        print('Case try end work')

    print('End programm')

except_zero_error()
