a = 3
b = 4
first = True
second = True
third = False

print('==, !=, >, <, >=, <=\n')
# ==
print('1(==)\n', first == second) # True
print(first == third) # False
print(a == b,'\n') # False

# !=
print('2(!=)\n', first != second) # False
print(first != third) # True
print(a != b, '\n') # True

# >
print('3(>)\n', first > second) # False
print(first > third) # True
print(a > b, '\n') # False

# <
print('4(<)\n', first < second) # False
print(first < third) # False
print(a < b) # True


# and, or, not, in
print('\nand, or, not, in')

print(first and second) # True
print(first and third) # False

print(first or second) # True
print(first or third) # True

print(not first) # False
print(not third) # True

message = 'Hello world, my friend'
word = 'friend'
print(word in message) # True
print(word not in message) # False
