'''
Ограничение времени	2 секунды
Ограничение памяти	256Mb

Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Алиса считает, что Боре нравятся только гаджеты, поэтому она решила почитать умных книжек по информатике. В одной из них она узнала понятия префикс и суффикс.

Префикс — это подстрока, начало которой совпадает с началом строки, а суффикс — это подстрока, конец которой совпадает с концом строки. Так, например, «ab» — один из префиксов строки «abacaba», а «25» — суффикс строки «ab125».

Алиса заметила у Бори в блокноте некоторую последовательность чисел, и ей стало интересно, существует ли хотя бы два, необязательно различных, числа таких, что один из префиксов первого равен одному из суффиксов второго.

К сожалению, эта задача оказалась для Алиса слишком сложной. Помогите Алисе в ее решении!


Формат ввода
В первой строке дано одно число n — количество чисел в блокноте. (1 ≤ n ≤ 1000)

Во второй строке записано n чисел ai — числа из блокнота. (1 ≤ ai ≤ 109)


Формат вывода
Выведите два числа x и y такие, что один из префиксов x-го числа в блокноте равен одному из суффиксов числа под номером y. Если таких двух чисел не существует, нужно вывести -1.
'''

def calculate_suf_and_pref() -> None:
    how_many_nums = int(input("Nums: "))
    nums = [int(input("")) for _ in range(how_many_nums)]


calculate_suf_and_pref()
