'''
range(stop)
range(start, stop)
range(start, stop, step)
'''

def range_in_cycles():
    for i in range(5):
        print(i, end=', ') # 0, 1, 2, 3, 4
    print('\n')

    for i in range(5, 11):
        print(i, end=', ') # 5, 6, 7, 8, 9, 10
    print('\n')

    for i in range(1, 11, 3):
        print(i, end=', ') # 1, 4, 7, 10
    print('\n')

    for i in range(10, 0, -2):
        print(i, end=', ') # 10, 8, 6, 4, 2, 0
    print('\n')


def range_in_cycles_and_lists():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end='\t')
        print('\n')

    numbers_100 = list(range(101))
    print(*numbers_100) # 0-100

range_in_cycles_and_lists()
