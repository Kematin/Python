def draw_triangle(a, b):
	count = 1
	for i in range(1, b + 1):
		print(' ' * (int(a / 2) - i + 1), end='')
		print('*' * count)
		count += 2

draw_triangle(15, 8)


def get_shipping_cost(quantity):
    if quantity > 1:
        return 1000 + (120 * (quantity - 1))
    else:
        return 1000
n = int(input())
print(get_shipping_cost(n))