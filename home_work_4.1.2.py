list_for_integers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print(f"Inputted list: {list_for_integers}")

modified_list = sorted(list_for_integers, key=lambda is_zero: is_zero == 0)

print(f"List with zeroes in the end: {modified_list}")

