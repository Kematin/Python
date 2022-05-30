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

    def get_procent(self, num) -> str:
        procent_1 = self.earnings / 100
        procent_from_num = round(num / procent_1, 2)
        return str(procent_from_num) + '%'

            
    def main(self):
        print('\t\t\tВсе значения писать в рублях')
        self.earnings = self.get_num('Ваш заработок: ')
        food = self.get_num('Ваш расход на питание: ')
        car = self.get_num('Ваш расход на транспортные средства: ')
        funny = self.get_num('Ваш расход на развлечения: ')
        utilities = self.get_num('Ваш расход на коммунальные услуги: ')
        clothes = self.get_num('Ваш расход на одежду: ')
        other = self.get_num('Остальные расходы: ')
        residue = self.earnings - sum([food, car, funny, utilities, clothes, other])

        print(f'\nВаш расход на еду состовляет {self.get_procent(food)} от заработка')
        print(f'Ваш расход на транспортные средства состовляет {self.get_procent(car)} от заработка')
        print(f'Ваш расход на развлечения состовляет {self.get_procent(funny)} от заработка')
        print(f'Ваш расход на коммунальные услуги состовляет {self.get_procent(utilities)} от заработка')
        print(f'Ваш расход на одежду состовляет {self.get_procent(clothes)} от заработка')
        print(f'Остальные ваши расходы составляют {self.get_procent(other)} от заработка')

        print(f'\nВаш остаток со всех расходов составляет {residue}')


def start():
    calculate = Finance()
    calculate.main()


if __name__ == '__main__':
    start()
