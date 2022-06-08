'''
match expression:
    case pattern_1:
        action_1
    case pattern_2:
        action_2
    case pattern_n:
        action:n
    case _:
        deffault action
'''


def hello(language):
    match language:
        case 'english': print('Hello')
        case 'russian': print('Привет')
        case 'german': print('Hallo')
        case _: print('Undefined')

languages = 'german', 'english', 'spanish', 'russian'
for l in languages:
    hello(l)
