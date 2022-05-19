num = 5
print(f'{num} in 2 base is {num:0b}')
print(f'{num} in 8 base is {num:0o}')


# Logical operations

# &
x1 = 2 # 010
y1 = 5 # 101
z1 = x1 & y1
print(f'{z1=}') # z1=0

x2 = 4 # 100
y2 = 5 # 101
z2 = x2 & y2
print(f'{z2=}') # z2=4
print(f'z2={z2:0b}') # z2=100

'''
0 * 1 = 0
1 * 0 = 0
0 * 1 = 0
z1 = 000 (in base 10 = 0)

1 * 1 = 1
0 * 0 = 0
0 * 1 = 0
z2 = 100 (in base 10 = 4)
'''

# |
x1 = 6 # 110
y1 = 2 # 010
z1 = x1 | y1
print(f'{z1=}') # 6
print(f'z1 in base 2 = {z1:0b}') # 110

'''
1 + 0 = 1
1 + 1 = 1
0 + 0 = 0
z1 = 110 (in base 10 = 6)
'''

# ^
x1 = 9 # 1001
y1 = 3 # 1100
z1 = x1 ^ y1
print(f'{z1=}\nz1 in base 2 = {z1:0b}') # 10 and 1010
'''
1 = 1 = 0
0 != 1 = 1
0 = 0 = 0
1 != 0 = 1
'''
