#factorial
def is_factorial(n):
    if n in (1, 0): return 1
    return is_factorial(n-1) * n

num = int(input('Введите число\n'))
print(is_factorial(num))
