#Вложенные циклы
for chas in range(24):
    if chas == 1:
        break
    for minute in range(60):
        for second in range(60):
            print(chas, ':', minute, ':', second)

'''
вложенный цикл выполняет все свои итерации для каждой отдельной итерации внешнего цикла;
вложенные циклы завершают свои итерации быстрее, чем внешние циклы;
для того, чтобы получить общее количество итераций вложенного цикла, надо перемножить количество итераций всех циклов.
'''


for i in range(8):
    for j in range(6):
        print('*', end='')
    print()


for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print()


for n in range(100):
    for k in range(100):
        for m in range(100):
            if 28 * n + 30 * k + 31 * m == 365:
                print('1 =', n, end ='\n')
                print('2 =', k, end ='\n')
                print('3 =', m, end ='\n\n~~~~\n')



for b in range(100):
    for k in range(100):
        for t in range(100):
            if (b * 10 + k * 5 + 0.5 * t == 100) and (b + k + t == 100):
                print('1 =', b, end ='\n')
                print('2 =', k, end ='\n')
                print('3 =', t, end ='\n\n')




