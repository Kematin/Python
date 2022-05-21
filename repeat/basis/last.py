# Type conversion

def type_conversion():
    a = '2'
    b = 3
    # print(a + b) error: can only concatenate str (not "int") to str

    print(int(a) + b) # 5
    print(a + str(b)) # 23
    print(float(a) + b) # 5.0

    print(int(False), int(True)) # 0 1
    print(int(4.5)) # 4



# global and local functions/variables

def global_local():
    name = 'Tom' # global variable in global_local()

    message = lambda: print('Hello', name) # we can use name in different functions
    message()

    def some_function(): # local function
        surname = 'Mark' # local variable

    # message = lambda: print('Hello', surname)  error: surname is not defiend
    # message()

    def global_name():
        global surname
        surname = 'Less'

    global_name()
    print('Hello', surname) # no error

    def outer():
        print('Without nonlocal (n=5 default in outer)')
        n = 5

        def inner():
            n = 25
            print(f'Inner = {n}')

        inner() # 25
        print(f'Outer = {n}') # 5

    outer()
    
    def outer_2():
        print('With nonlocal (n=5 default in outer)')
        n = 5

        def inner():
            nonlocal n
            n = 25
            print(f'Inner = {n}')

        inner() # 25
        print(f'Outer = {n}') # 25

    outer_2()


# some_function() error: some_finction() is not defiend



# closure
def closure():
    
    def clouse(n):

        def double():
            nonlocal n
            n *= 2
            print(n)

        return double

    a = clouse(3) # a() = double() 
    a() # 6
    a() # 12
    a() # 24

    def multiply(n):
        return lambda m: n * m

    fn = multiply(4)
    print(fn(5)) # 20
    print(fn(10)) # 40

closure()
