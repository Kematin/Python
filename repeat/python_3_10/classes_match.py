class UserInput:
    def __init__(self, action: str, value: int):
        self.action = action
        self.value = value


def run_horizontaly(user_input):
    match user_input:
        case UserInput(action='left' | 'right', value=int(value)):
            print(f'Run horizontaly to {value}px')
        case {'action': 'left' | 'right', 'value': int(value)}:
            print(f'Run horizontaly to {value}px')
        case _:
            print('Wrong command')
            
input_1 = UserInput('right', 64)
input_2 = UserInput('top', 100)
input_3 = {
    'id': 1591524,
    'name': 'Robert',
    'action': 'left',
    'cash': 1_000_000,
    'value': 80
}
inputs = input_1, input_2, input_3
for i in inputs:
    run_horizontaly(i)
