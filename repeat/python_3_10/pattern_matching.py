def run_old(user_input: list) -> None:
    if isinstance(user_input, list) and len(user_input) == 2:
        command, value = user_input
        print(f'{command=}\n{value=}')
    else:
        print('Uncorrect user input')
# run_old('go_left 100'.split())


# with pattern matching
def run(user_input: list) -> None:
    match user_input:
        case 'top', value if int(value) > 100:
            print('something...')
        case 'left' | 'top' | 'bottom' | 'right' as command, value:
            print(f'Go to {command} to {value}m')
        case 'shoot', *coords:
            print(f'Shoot by coords: {coords}')
        case 'quit',:
            print('Quit')
        case _:
            print('Wrong Command')

def action():
    run('top 200'.split())
    run('right 42'.split())
    run('shoot 533 100 200 600 1000'.split())
    run('gadg 533 600 1000'.split()) # Wrong Command
    run('quit'.split())



user = {
    'id': 1591524,
    'name': 'Robert',
    'action': 'bottom',
    'cash': 1_000_000,
    'value': 80
}

def run_user(user_input: dict) -> None:
    match user_input:
        case {'action': 'left' | 'top' | 'right' | 'bottom' as action, 'value' : int(value)}:
            print(f'{action=}, {value=}')
        case _:
            print('Nothing')

run_user(user)
