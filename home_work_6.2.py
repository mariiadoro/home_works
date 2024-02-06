my_dict_1 = {1:1, 2:2}
my_dict_2 = {11:11, 2:22}

# а) Створити список із ключів, які є в обох словниках.
key_in_both = [key for key in my_dict_1 if key in my_dict_2]
print(key_in_both)

# б) Створити список із ключів, які є у першому, але немає у другому словнику.
key_in_my_dict_1 = [key for key in my_dict_1 if key not in my_dict_2]
print(key_in_my_dict_1)

# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
new_dict = {key: my_dict_1[key] for key in my_dict_1 if key not in my_dict_2}
print(new_dict)

# г) Об'єднати ці два словники у новий словник за правилом:
united_dict = {}

for key, value in my_dict_1.items():
    if key in my_dict_2:
        united_dict[key] = [value, my_dict_2[key]]
    else:
        united_dict[key] = value

for key, value in my_dict_2.items():
    if key not in my_dict_1:
        united_dict[key] = value

print(united_dict)
