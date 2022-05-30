print('Hello in chislovaya ugodayka, zagaday chislo')

def is_valid(n):
    if n.isdigit():
        if int(n) > 0: return True
        else: return False
    else: return False

def main(n: int):
    check = input(f'Vashe chislo bolshe {n // 2}? (+ dlya da, - dlya net, = dlya ravno) ') 
    if check == '+':
        n = (n//2)//2
        print(n)

num = input('\nGranica chisla ').strip()
while not is_valid(num):
    num = input('Vvedeno nekkorektnoe chislo: ')
    

main(int(num))
