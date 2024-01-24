print("Let`s make some calculations!")

while True:
    number_first = input("Please, input first integer number: ")
    if '.' in number_first:
        try:
            num_first_typed = float(number_first)
            break
        except ValueError:    # Я знаю, що ми цього щє не вивчали, але я трохи погуглила, тож вирішила використати це "expect", щоб програма виглядала краще та працювала і з int, і з float
            print("Please, do not input words or other symbols! Try again")
    elif number_first.isdigit():
        num_first_typed = int(number_first)
        break
    else:
        print("Please, do not input words! Try again")

while True:
    math_function = input("Please, choose math function: ")
    if math_function == "+" or math_function == "-" or math_function == "*" or math_function == "/":
        break
    else:
        print("Please input one of this functions: +, -, *, /")

while True:
    number_second = input("Please, input second integer number: ")
    if "." in number_second:
        try:
            num_second_typed = float(number_second)
            break
        except ValueError:
            print("Please, do not input words or other symbols! Try again")
    elif number_second.isdigit():
        num_second_typed = int(number_second)
        break
    else:
        print("Please, do not input words! Try again")

if math_function == "-":
    result = num_first_typed - num_second_typed
elif math_function == "+":
    result = num_first_typed + num_second_typed
elif math_function == "*":
    result = num_first_typed * num_second_typed
elif math_function == "/":
    if num_second_typed != 0:
        result = num_first_typed / num_second_typed
    else:
        print("You can not divide on 0, don`t you know that? Great, you broke EVERYTHING, the world is COLIDED!!!!! It was a joke... just start the program again")
        exit()

print(f"Result is: {result}")
