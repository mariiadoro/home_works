def difference_between_numbers(*args):
    if not args:
        return 0
    difference = max(args) - min(args)
    return round(difference, 2)

assert difference_between_numbers(1, 2, 3) == 2, 'Test1'
assert difference_between_numbers(5, -5) == 10, 'Test2'
assert difference_between_numbers(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference_between_numbers() == 0, 'Test4'
print('OK')