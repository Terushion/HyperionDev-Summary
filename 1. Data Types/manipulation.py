# mainpulation.py

"""

"""

# The program will ask the user to input any sentence of their choice to start with

# Get sentence to manipulate
str_manip = input("Hi, there! Please enter a sentence of your choice: ")
print()

print(len(str_manip))   # prints out the length of the sentence that the user had input
print()

print(str_manip.replace("", "@"))   # prints out variable but will replace the last letter in the sentence with '@'
print()

print(str_manip[-1:-4:-1]) # will print out the last three characters in reverse
print()

# A 5-letter word made up of the first 3 letters and the last 2 letters
print((str_manip[0:3] + str_manip[-2:])) 
