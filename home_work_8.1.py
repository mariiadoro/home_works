def add_one(some_list):
    new_integer = int(''.join(str(digit) for digit in some_list))
    new_integer += 1
    to_list = [int(number_in_list) for number_in_list in str(new_integer)]
    return to_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")