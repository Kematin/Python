from random import choice

welcome = print('Добро Пожаловать в игру "камень, ножницы, бумага"')
types = ['к' , 'н' , 'б']
types_for_bot = ['камень' , 'ножницы' , 'бумагу']

flag = '+'

while flag == '+':
   type = input('Для начала выбери свой предмет (к = камень, н = ножницы, б = бумага)\n')

   while type not in types:
       type = input('Вы выбрали неккоректный предмет\n')

   types_bot = choice(types_for_bot)

   while types_bot[0] == type:
       type = input('Упс! У вас ничья, попробуйте ещё\n')
       types_bot = choice(types_for_bot)

   if types_bot[0] == 'к' and type == 'б':
        print('Вы победили! Бот выбрал камень')
        

   elif types_bot[0] == 'к' and type == 'н':
        print('Увы, но вы проиграли! Бот выбрал камень')
        

   elif types_bot[0] == 'б' and type == 'к':
        print('Увы, но вы проиграли! Бот выбрал бумагу')
        

   elif types_bot[0] == 'н' and type == 'б':
        print('Увы, но вы проиграли! Бот выбрал ножницы')
        

   elif types_bot[0] == 'б' and type == 'н':
        print('Вы победили! Бот выбрал бумагу')
        

   elif types_bot[0] == 'н' and type == 'к':
        print('Вы победили! Бот выбрал ножницы')
        
   flag = input('Введите + если желаете сыграть ещё раз\n')

else:
    print('\nСпасибо, что сыграл!')
    end = input()