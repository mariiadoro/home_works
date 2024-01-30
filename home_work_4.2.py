my_list = [0, 1, 7, 2, 4, 8]
element_sum = 0

for element_in_list in range(0,len(my_list),2):
    element_sum += my_list[element_in_list]

multiple_on_last_element = element_sum * my_list[-1]


print(multiple_on_last_element)


