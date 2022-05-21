# Function as a type

def functions_as_a_type():
    def say_hello(): print('Hello')
    def say_bye(): print('Bye')
        
    messages = say_hello, say_bye
    for message in messages:
        message()

    def sum_nums(a, b): return a + b
    def multiply(a, b): return a * b

    x, y = 4, 5
    operations = sum_nums, multiply
    for result in operations:
        print(result(x, y))


# Function as a function parameter

def function_as_a_parameter():
    def sum_nums(a, b): return a + b
    def multiply_nums(a, b): return a * b

    def nums_manipulation(a, b, *, operation):
        print(f'result = {operation(a, b)}')

    x, y = 15, 32

    nums_manipulation(x, y, operation=sum_nums)
    nums_manipulation(x, y, operation=multiply_nums)



# The function as a result of the function

def function_as_a_result():
    
    def sum_nums(a, b): return a + b
    def subtract(a, b): return a - b
    def multiply(a, b): return a * b

    check = input('Select operation:\n1 - subtract (-)\n2 - sum (+)\n3 - multiply (*)\n:')
    a = int(input('Num 1: '))
    b = int(input('Num 2: '))

    def select_choice(choice, a, b):
        if choice in ('1', '-'):
            return subtract(a, b)

        elif choice in ('2', '+'):
            return sum_nums(a, b)
        elif choice in ('3', '*'):
            return multiply(a, b)

        else: return "error"

    result = select_choice(check, a, b)
    print(f'{result=}')



# lambda

def lambda_function():
    '''
    lambda [parameter]: instruction
    '''

    def message(): print('Hello blo')
    # =
    message_2 = lambda: print('Hello blo')

    message()
    message_2()


    a = int(input('Num 1: '))
    b = int(input('Num 2: '))

    result = lambda a, b: a + b 
    print(f'result = {result(a, b)}')

    def nums_manipulation(a, b, operation):
        print(f'result = {operation(a, b):.2f}')

    nums_manipulation(a, b, lambda a, b: a - b) 
    nums_manipulation(a, b, lambda a, b: a * b) 
    nums_manipulation(a, b, lambda a, b: a ** b) 
    nums_manipulation(a, b, lambda a, b: a / b) 


lambda_function()
