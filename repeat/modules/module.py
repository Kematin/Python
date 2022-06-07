variable = 'Hello world'

class Commands:
    def print_message(self, message):
        print(f'Your message:\n{message}')
    
    double = lambda self, x: x * 2
    sum_nums = lambda self, x, y: x + y
    sub = lambda self, x, y: x - y
    multiply = lambda self, x, y: x * y

    def return_commands(self, x, y):
        print(f'{x} * 2 = {self.double(x)}') 
        print(f'{x} - {y} = {self.sub(x, y)}') 
        print(f'{x} + {y} = {self.sum_nums(x, y)}') 
        print(f'{x} * {y} = {self.multiply(x, y)}') 


secret = lambda: print('Secret')

# Anything written in this piece of code will 
# not be executed when this module is imported
if __name__ == '__main__':
    secret()
    command = Commands()
    command.return_commands(5, 2)
