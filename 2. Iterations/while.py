''' Practical task one '''

"""
Follow these steps:

    ● Create a file called while.py.
    ● Write a program that continually asks the user to enter a number.
    ● When the user enters “-1”, the program should stop requesting the user
    to enter a number,
    ● The program must then calculate the average of the numbers entered,
    excluding the -1.
    ● Make use of the while loop repetition structure to implement the
    program.
    
"""

# Program will ask user to continously input a number unless that number is -1
num = 0 # Num is set to 0 as it has to be defined and so that the calculations are correct
sum1 = 0    # This variable will collect the sum of all the numbers the user had input
# if '-1' was the first input, then the sum will be 0
count = 0   # This will record each time the user makes an input
# Below, is a while loop that will keep running as long as the input made isn't -1. 

while num != -1:
    num = int(input("Please input a number and when you wish to end the loop, enter -1:\n "))
    print()
    sum1 += num
    count += 1
 
if num == -1:
    sum1 += 1
    count -= 1
    print(f"The sum of all the numbers you have entered amounts to {sum1} \n")
    print(F"And the average of the sum ({sum1} divded by {count}) is {sum1 / count} \n")

# When -1 is entered, the program will output the sum of the numbers entered beforehand if there was any.