new_list = []
print(f"Initial list -> {new_list}")
if len(new_list) > 1:
    last_element = new_list.pop(-1)
    new_list.insert(0, last_element)

print(f"Modified list -> {new_list}")
