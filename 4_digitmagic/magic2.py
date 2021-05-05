message= "In this magic we will tell you the number which you have omitted in the step 4 without ever getting the input from you \nlets start..."
print(message.upper())
print('''STEP 1. Choose any 4 digit number\n
STEP 2. Reverse your number\n
STEP 3. Subtract the smaller number from the other number\n
STEP 4. From the answer ommit/Hide any number(digit)\n
''')
number= input("Tell me the remaing numbers after ommiting a digit in step4:")
sum_of_digits = sum(int(digit) for digit in str(number))
if sum_of_digits % 9 == 0:
    Input=input("is the number hidden/ommited is greater than 5?\nPress Y for Yes: \nPress N for No:")
    #fahrenheit = float (input("what tempreture(in fahrenheit) would you like converted to celsius?: "))
    print(Input)
    if Input == "y":
        print("your hidden/omitted number is 9")
    else:
        print("your hidden/omitted number is 0")

elif sum_of_digits < 9:
    y=your_num = 9 - sum_of_digits
    print(y)
elif sum_of_digits > 9:
    y=your_num = 18 - sum_of_digits
    print(y)
elif sum_of_digits >18:
    y=your_num = 27  - sum_of_digits
    print(y)
elif sum_of_digits >27:
    y=your_num = 36 - sum_of_digits
    print(y)
elif sum_of_digits >36:
    y=your_num = 45 - sum_of_digits
    print(y)
elif sum_of_digits >45:
    y=your_num = 54 - sum_of_digits
    print(y)
elif sum_of_digits >54:
    y=your_num = 63 - sum_of_digits
    print(y)
elif sum_of_digits >63:
    y=your_num = 72 - sum_of_digits
    print(y)
elif sum_of_digits >72:
    y=your_num = 81 - sum_of_digits
    print(y)
elif sum_of_digits >81:
    y=your_num = 90 - sum_of_digits
    print(y)
elif sum_of_digits >90:
    y=your_num = 99 - sum_of_digits
    print(y)

input("print ENTER to Exit")