while True:
    four_digit_number = input("Input a four-digit number: ")
    if len(four_digit_number) == 4 and four_digit_number.isdigit():
        break
    else:
        print("Please, input four-digit integer number!")

digit_1 = int(four_digit_number) % 10
digit_2 = (int(four_digit_number) % 100) // 10
digit_3 = (int(four_digit_number) % 1000) // 100
digit_4 = int(four_digit_number) // 1000

print(digit_4)
print(digit_3)
print(digit_2)
print(digit_1)

# also will work with this one:)
# for i in range(len(four_digit_number)):
#   print(four_digit_number[i])
