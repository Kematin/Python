from random import choice
import string

class GenerateData:
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

    def generate_email(self):
        letters = ''.join(choice(self.letters) for _ in range(5))
        digits = ''.join(choice(self.digits) for _ in range(4))
        email = 'Email_Rambler_' + letters + digits
        return email

    def generate_secret_word(self):
        words = [
            "Аджапсандали",
            "Адобо",
            "Азу",
            "Аквакотта",
            "Аперитив",
            "Ачма",
            "Аш",
            "Ашуре",
            "Баба",
            "Багет",
            "Балиш",
            "Безе",
            "Беккен",
            "Бекон",
            "Бигос",
            "Блин",
            "Борщ",
            "Ботвинья",
            "Брик",
            "Брускетта",
            "Булка",
            "Бургер",
            "Бутерброд",
            "Вареники",
            "Варенье",
            "Васаби",
            "Ватрушка",
            "Вафля",
            "Ветчина",
            "Виндалу",
            "Винегрет",
            "Второе блюдо",
            "Выпечка",
            "Газмах",
            "Галантин",
            "Гарнир",
            "Голубцы",
            "Горячие блюдо",
            "Гравлакс",
            "Гратен",
            "Грильяж",
            "Губадья",
            "Гуляш",
            "Десерт",
            "Джем",
            "Долма",
            "Донбури",
            "Драник",
            "Ёжики",
            "Ека",
            "Жаркое",
            "Желе",
            "Жульен",
            "Закуска",
            "Заливное",
            "Запеканка",
            "Зефир",
            "Зразы",
            "Икра",
            "Йогурт",
            "Йока",
            "Йох",
            "Калитка",
            "Калья",
            "Канапе",
            "Канеле",
            "Кассуле",
            "Каша",
            "Кекс",
            "Кетчуп",
            "Кефир",
            "Киш",
            "Клёцки",
            "Коврижка",
            "Колбаса",
            "Компот",
            "Конфета",
            "Коржик",
            "Котлета",
            "Кофе",
            "Кошари",
            "Крем",
            "Крем-брюле",
            "Крем-суп",
            "Круассан",
            "Кулебяка",
            "Кулеш",
            "Кулич",
            "Кунь-аман",
            "Курник",
            "Лазанья",
            "Лангет",
            "Лепешка",
            "Лобио",
            "Макарон",
            "Мармелад",
            "Маффин",
            "Медовик",
            "Мороженое",
            "Морс",
            "Мусс",
            "Накрепок",
            "Напиток",
            "Наполеон",
            "Окрошка",
            "Оладья",
            "Оливье",
            "Омлет",
            "Паста",
            "Пастьера",
            "Паштет",
            "Пельмени",
            "Перемяч",
            "Печенье",
            "Пирог",
            "Пирожное",
            "Пирожок",
            "Пицца",
            "Плов",
            "Пончик",
            "Похлебка",
            "Профитроль",
            "Пряник",
            "Пудинг",
            "Пюре",
            "Рагу",
            "Рамэн",
            "Рассольник",
            "Расстегай",
            "Рататуй",
            "Ризотто",
            "Ролл",
            "Рулет",
            "Салат",
            "Самса",
            "Соба",
            "Солянка",
            "Соус",
            "Сочень",
            "Сочник",
            "Стейк",
            "Студень",
            "Суп",
            "Суши",
            "Сыр",
            "Сэндвич",
            "Такос",
            "Такояки",
            "Тарт",
            "Тартин",
            "Тартифлет",
            "Творожник",
            "Тефтели",
            "Торт",
            "Тост",
            "Трюфель",
            "Тюря",
            "Угали",
            "Удон",
            "Урама",
            "Урбенес",
            "Урбеч",
            "Уха",
            "Флёр-де-сель",
            "Форшмак",
            "Фрикадельки",
            "Фрикассе",
            "Фуль",
            "Фуфу",
            "Харчо",
            "Хачапури",
            "Хворост",
            "Хингалш",
            "Хлеб",
            "Холодец",
            "Холодник",
            "Холодник",
            "Хумус",
            "Цимес",
            "Цкан",
            "Чай",
            "Чапати",
            "Чаудер",
            "Чебурек",
            "Чизкейк",
            "Шаньга",
            "Шарлотка",
            "Шашлык",
            "Шеффердс-пай",
            "Шницель",
            "Штрудель",
            "Щи",
            "Ынджера",
            "Эклер",
            "Эчпочмак",
            "Юка",
            "Юшка",
            "Якисоба",
            "Якитори",
                        ]
        word = choice(words)
        return word


def start():
    gen = GenerateData()
    password = gen.generate_password(30)
    login = gen.generate_login()
    email = gen.generate_email()
    secret = gen.generate_secret_word()
    print(f'{login}\n{password}')
    print(f'{email}\n{secret}')

if __name__ == '__main__':
    start()
