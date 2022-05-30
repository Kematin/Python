# in this block

# types of variables
# pep 8 for variables
# Registry Dependence
# f line and format



# types of variables

name = 'Mark' # string
num = 4 # intenger
drob_num = 4.24 # float
bool_value = True # bool
complex_number = 1 + 43j # complex

print(name, num, drob_num, bool_value, complex_number)


# pep 8 for variables

name = 'Tom' # good
dkgjadghqiwjg = 'Tom' # bad

name_of_family_1 = 'Romanov' # good (underscore notation)
nameOfFamily1 = 'Romanov' # bad (camel case)


# the variable cannot be named with built-in names

'''
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
'''


# Registry Dependence

name = 'Tom'
Name = 'Mark'
print(name) # Tom
print(Name) # Mark


# Bool

is_married = False
is_alive = True

if is_married: print('They are married')
else: print('they are not married') # will print

if is_alive: print('he is alive') # will print
else: print('he isn`t alive')

print(is_married) # False
print(not is_married) # True


# Intenger

age = 21 # base-10
b = 0b1011 #base-2
c = 0o431 #base-8
d = 0x2A #base-16

print(age) # 21
print(b) # 11
print(c) # 281
print(d) # 42


# Float

a = 45.51
x = 3.9e3
y = 3.9e-3

print(a) # 45.51
print(x) # 3900.0
print(y) # 0.0039


# String

trible_x = 'x'
print(trible_x * 3) # xxx


# \t = 4 space before line
# \n = new line
# \" or \' = create " in line
# print("name is "Tom"") will error

text = f"Your message:\n\"{input('Write your message: ')}\"\tgood message :)"
print(text)

''' will print

Write your message:
Your message:
"message"    good message :)

'''

path_1 = "C:\python\name.txt" 
path_2 = r"C:\python\name.txt"

print(path_1)
# C:\python
# ame.txt

print(path_2)
# C:\python\name.txt


# f line and format

name = 'Some name'
age = 25

print(f'Your name {name} and your age {age}')
print('Your name {name} and your age {age}'.format(name=name, age=age))
