# numbers.py

"""
Follow these steps:

● Create a new Python file called numbers.py.
● Ask the user to enter three different integers.
● Then print out:
    ○ The sum of all the numbers
    ○ The first number minus the second number
    ○ The third number multiplied by the first number
    ○ The sum of all three numbers divided by the third number
"""

# Program will ask user to input three different integers


num1 = int(input("Please input the first integer you would like: "))
print()

num2 = int(input("Please input another integer but it has to be different from the last one: "))
print()

num3 = int(input("Please input the last integer but it has to be different from the first two: "))
print()

# The sum of all the numbers

sum_of_num = num1 + num2 + num3
print(f"The sum of all the numbers you chose is {sum_of_num}")
print()

# The first number minus the second number
# e.g. num1 - num2

second_prob = num1 -num2
print("{} minus {} equals {}".format(num1, num2, second_prob))
print()

# The third number multiplied by the first number 
# e.g. num3 * num1

third_prob = num3 * num1 
print("{} multiplied by {} equals {}".format(num3, num1, third_prob))
print()

# The sum of all three numbers divided by the third number 
# e.g. (num1 + num2 + num3) / num3

fourth_prob = sum_of_num / num3
print(f"The sum of all the numbers you chose divided by {num3} is {fourth_prob}")
print()
 # type: ignore