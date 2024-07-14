""" Practical Task One"""

"""
Write a function to calculate the sum of numbers in a list
up until and including the given index point by
making use of recursion rather than loops.
Example: list = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10 , 11], so
sum_recursion(5) should return 1 + 2 + 3 + 4 + 5 + 6 = 21

or 
other_sum([1, 4, 5, 3, 12, 16], 4)
 => 25
"""

print("\nThe first recursion method:\n")

def sum_recursion(index):
    # List
    integer_list = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10, 11]

    # Base case: if index is 0, return the value at index 0
    if index == 0:
        return integer_list[0]
    # Recursive case: sum the current value with the sum of the values before it
    # calculates sum of numbers up till index
    else:
        return integer_list[index] + sum_recursion(index - 1)
    # As the function is called again, the index is one less than initally
    # essentially this would be the same as as '+=' in a for loop,
    # where information are stored in a variable and then more 
    # information are added as the loop iterates until finished
    

# sum_recursion(2)   # expected output: 1+2+3 = 6
#  OR
index = int(input("There is currently a list of numbers from 1 to 11.\n"
              "please input an index to see the sum of all the "
               "numbers up until AND, including that same index: "))

total = (sum_recursion(index))
print(f"The total sum is {total}.\n")




# SECOND METHOD

print("The second recursion method:")
def other_sum(integers, index):
    # Base case: if index is 0, return the value at index 0
    if index == 0:
        return integers[0]
    # Recursive case: sum the current value with the sum of the values before it
    else:
        return integers[index] + other_sum(integers, index - 1)
    # calculates sum of numbers up till index

total = (other_sum([5, 6, 3, 12, 7, 4, 2], 4))
print(f"the total sum is {total}.")


# OR another method below but comment out line 27 & 28

# integers = []

# def list_input():

"""
Here, we want to allow the user to choose how elements they want to
add in a list and what those elements are (integers)
We store both the list and the length of the list as two seperate values
this way we then can enter those variables in the parameters when we call
the original function 'other_sum'.
The user can also choose the index that they want the function to calculate
the sum up until and including that index

"""

#     count = 0
#     integer_num = 1
#     length = int(input("Enter the number of integers\n"
#                         "you want your list to contain, up to 10:\n"))
    
#     while count != length:
#         # if count doesn't equate to length then code below will run
#         num = int(input(f"\nPlease enter a integer {integer_num} to add to your own list: "))
#         count += 1
#         integer_num += 1
#         integers.append(num)

#     return integers

# list_input()

# import time
# time.sleep(0.5)

# index = int((input("\nPlease input an index to see the sum of all the "
#                "numbers up until AND, including that same index: ")))

# print(other_sum(integers, index))