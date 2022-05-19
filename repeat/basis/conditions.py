'''
if conditions:
    action
[elif conditions:
    action]
[else:
    action]
'''

some_word = 'gold'
some_word_2 = 'world'
message = 'Au = gold'

if some_word in message:
    print(f'{some_word} in message') # will output

if some_word_2 in message:
    print(f'{some_word_2} in message')
else:
    print(f'{some_word_2} not in message') # will output


num = int(input('Your num is: '))
if num == 101:
    print(f'it`s True num ')


name = 'Tom'

if name == 'Jerry':
    print('Your name is Jerry!')

elif name == 'Mark':
    print('Your name is Mark')
elif name == 'Tom':
    print('Your name is Tom!')

else: print('idk your name :(')

age = 51

if name == 'Jerry':
    print('Your name is Jerry!')

elif name == 'Mark':
    print('Your name is Mark')
elif name == 'Tom':
    print('Your name is Tom!')

    if age in (10, 50, 51, 20):
        print(f'Your age is {age}')

else: print('idk your name :(')
