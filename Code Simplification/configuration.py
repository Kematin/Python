class User():
	def __init__(self, group: str):
		self.group = group


def bad_code(user):
	if user.group == 'admin':
		return 5
	elif user.group == 'client':
		return 4
	elif user.group == 'manager':
		return 10

def good_code(user):
	group_to_procces = {
		'admin': 5,
		'client': 4,
		'manager': 10
	}
	return group_to_procces[user.group]

if __name__ == '__main__':
	user = User(group='admin')
	print(good_code(user))
