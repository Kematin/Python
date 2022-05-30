class Finance:

    def is_num(self, num) -> bool:
        if not num.isdigit(): 
            return False
        elif int(num) < 0: 
            return False
        else: return True


    def get_num(self, text) -> int:
        some_number = input(text)
        while not self.is_num(some_number):
            some_number = input(f'Введено неверное значение\n{text}')

        return int(some_number)

    def get_procent(self) -> str:
        pass

            
    def main(self):
        print('\t\t\tВсе значения писать в рублях')
        earnings = self.get_num('Ваш заработок: ')
        food = self.get_num('Ваш расход на питание: ')
        car = self.get_num('Ваш расход на транспортные средства: ')
        funny = self.get_num('Ваш расход на развлечения: ')
        utilities = self.get_num('Ваш расход на коммунальные услуги: ')
        clothes = self.get_num('Ваш расход на одежду: ')
        other = self.get_num('Остальные расходы: ')


def start():
    calculate = Finance()
    calculate.main()


if __name__ == '__main__':
    start()
