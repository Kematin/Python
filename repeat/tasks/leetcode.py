'''
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
'''

def roman_to_int(s:str) -> int:
    nums = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
            }

    double_nums = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
            }
    total = 0

    for el in double_nums:
        total += s.count(el) * double_nums[el]
        if s.count(el) != 0:
            s = s[:s.find(el)] + s[s.find(el) + 2:]

    for el in s:
        total += nums[el]

    return total

# word = 'III'
# print(f'{word} in numbers = {roman_to_int(word)}')

def is_palindrome(s: str) -> bool:
    for el in range(len(s) // 2):
        if s[el] != s[-el - 1]: return False
    return True

# word = '24519836517836981368136146'
# if is_palindrome(word):
#     print(f'{word} = palindrome')
# else: print(f'{word} not is palindrome')
