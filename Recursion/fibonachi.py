#fibonachi
def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    a = fib(n-2)
    b = fib(n-1)
    return a + b

num = int(input('Введите число\n'))
print(fib(num))
