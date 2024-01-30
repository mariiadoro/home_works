# Just a little bit of practice, how to check the list only for integers
# valid_input = False
# while not valid_input:
#     new_list = input("Enter a list of integer numbers with spaces, for example: 0 1 0 12 3:\n ")
#
#     list_for_integers = []
#
#     for item_in_list in new_list.split():
#         if item_in_list.isdigit():
#             list_for_integers.append(int(item_in_list))
#         else:
#             print("This list should contain only integers, without any symbols and letters! Please try again: ")
#             break
#     else:
#         valid_input = True

list_for_integers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print(f"Inputted list: {list_for_integers}")
list_without_zeroes = []
zeros_list = []

for integer_item in list_for_integers:
    if integer_item == 0:
        zeros_list.append(integer_item)
    else:
        list_without_zeroes.append(integer_item)
modified_list = list_without_zeroes + zeros_list
print(f"List with zeroes in the end: {modified_list}")





