import keyword
import string

result = True

inputted_string = input("Please, input the name for variable: ")

first_is_digit = inputted_string[0].isdigit()
inputted_is_digit = inputted_string.isdigit()
contains_upper = any(string_element.isupper() for string_element in inputted_string)
contains_keywords = inputted_string in keyword.kwlist
contains_space = ' ' in inputted_string
contains_punctuation = any(string_element in string.punctuation and string_element != '_' for string_element in inputted_string)

if not first_is_digit and not inputted_is_digit and not contains_upper and not contains_keywords and not contains_space and not contains_punctuation:
    result = True
else:
    result = False

print(result)
