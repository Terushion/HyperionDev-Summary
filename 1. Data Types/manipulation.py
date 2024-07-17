# mainpulation.py

"""
Follow these steps:
● Create a new Python file in the Dropbox folder for this task and call it
manipulation.py.

● Ask the user to enter a sentence using the input() function. Save the user's
response in a variable called str_manip.

● Using this string value, write the code to do the following:

    ○ Calculate and display the length of str_manip.
    ○ Find the last letter in str_manip sentence. Replace every occurrence
    of this letter in str_manip with '@'.
    ■ e.g. if str_manip = “This is a bunch of words”,
     the output would be: “Thi@ i@ a bunch of word@”

○ Print the last three characters in str_manip backwards.

    ■ e.g. if str_manip = “This is a bunch of words”, the output would
    be: “sdr”.

○ Create a five-letter word that is made up of the first three characters
and the last two characters in str_manip.

    ■ e.g. if str_manip = “This is a bunch of words”, the output would
    be: “Thids”.

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
