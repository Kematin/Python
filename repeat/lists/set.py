'''
set = {value1, value2, ..., valueN}
set contains only unique values.
'''

def def_set():
    users = {'Tom', 'Bob', 'Mark', 'Bob'}
    print(users) # Tom, Bob, Mark

    nums = [5, 1, 531, 46, 1]
    nums_set = set(nums)
    nums_set.add(4)
    print(nums_set) # {1, 4, 5, ...}

    nums_set.remove(5)
    print(nums_set) # {1, 4, ...}

    # nums_set.remove(6) KeyError
    nums_set.discard(6) # nothing


if __name__ == '__main__':
    def_set()
