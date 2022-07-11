from random import choice
import string

class GeneratePassword:

    def __init__(self):
        self.letters = list(string.ascii_letters)
        self.digits = [str(i) for i in range(10)]

    def generate_password(self, len_):
        main_list = self.letters + self.digits
        password = ''.join(choice(main_list) for _ in range(len_))
        return password

    def generate_login(self):
        letters = ''.join(choice(self.letters) for _ in range(5))
        digits = ''.join(choice(self.digits) for _ in range(4))
        login = 'Profile_' + letters + digits
        return login


def start():
    gen = GeneratePassword()
    password = gen.generate_password(30)
    login = gen.generate_login()
    print(f'{login}\n{password}')

if __name__ == '__main__':
    start()
