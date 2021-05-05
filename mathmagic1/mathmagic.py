message= "In this magic we will tell you the number which you have guessed in the begining without ever getting the input from you \nlets start..."
print(message.upper())
print("STEP 1. choose any whole number")
print("STEP 2. Multiply your number with 2")
print("STEP 3. Add 2 after multiplication")
print("STEP 4. Multiply it by 5")
print("STEP 5. Now substract 5 from it")
number=input("what is your final number: ")
num = str(number)
mun= num[::-1]
trunum=mun[1::]
final_num=trunum[::-1]
print("Your number is: 0",final_num)

input('Press ENTER to exit')
