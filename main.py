'''===============================================================================================
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate
message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.

Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


==============================================================================================='''

'''===============
    Base Challenge
   ==============='''

print("base challenge and extra #1\n================")

user_num = int(input('Enter a number: '))
if user_num % 2 == 0:
    print(user_num, "is an even number.")
else:
    print(user_num, "is an odd number.")

'''=====================
     Extra Challenge 1
   ====================='''

if user_num % 4 == 0:
    print(user_num, "is a multiple of 4")

print("==========\n extra #2 \n==========")

num = int(input("Enter a number: "))
check = int(input("Enter a smaller number: "))

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)