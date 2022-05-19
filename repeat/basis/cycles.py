# while and for

'''
while conditions:
    action

for i in range():
    action
'''


# while

num = 1
while num <= 5:
    print(f'{num=}')
    num += 1
print('End cycle')


# for

for i in range(5):
    print(f'num = {i}')

word = 'Hello my N-word'
for symbol in word:
    print(symbol)


# break

num = 0
while num <= 6:
    print(f'number = {num}')
    if num > 5:
        print('error')
        break
    num += 1


for i in range(10):
    if i == 3: break
    print(f'{i=}')


# else

for i in range(1, 10, 2):
    print(f'{i=}')
else:
    print(f'last number = {i}\n\tEnd cycle.')
    

# nested cycles

j = 1
for i in range(1, 11):
    while j < 10:
        print(i*j, sep='\t')
        j += 1
    print('\n')
    j = 1
else:
    print('\tEnd cycle.')


# continue 

for i in range(20):
    if i in (1, 3, 7, 11, 13, 17):
        continue
    print(f'{i=}')
else:
    print('\tEnd cycle.')
