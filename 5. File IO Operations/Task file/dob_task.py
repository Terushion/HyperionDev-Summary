# Practical Task 1

"""
● Create a new Python file in the Dropbox folder for this task, and call it
dob_task.py.
● In your Python file, write a program that reads the data from the text file
provided (DOB.txt) and prints it out in two different sections in the format
displayed below:

        Name
        Orville Wright
        Rogelio Holloway
        Marjorie Figueroa
        … etc.
        
        Birthdate
        21 July 1988
        13 September 1988
        9 October 1988
        … etc.

Note: Remember to ensure that the text folder is in the appropriate file directory
or Python won’t be able to find it when running your program. Get this right first
by running the example files, and then do the task.
"""

# We have created two empty variables to allocate certain parts of,
# the information we're going to read, we'll use the variables,
# to print the information under two sections
# The information taken will be stored as lists in both variables

names = []
birthdates = []

# Using the with/as and open() function, 
# this file below will open
# The mode we'll use is 'r+'
# This mode will allow user to read and write,
# but if the file that we will open didn't exist,
# it would create an I/O error

with open('DOB.txt', 'r+') as file:
        for line in file:       # We are using for loop to iterate through each line
                sentence = line.split()
                # each line will be split into list of strings    
                # Below we will create two local variables to store the info we want
                # first two elements will be assigned to full_name for each iteration
                # the same will happen for the date of births but
                # it will be the last three elements in the list of strings
                full_name = sentence[0] + " " + sentence[1]
                dob = sentence[2] + " " + sentence[3] + " " + sentence[4]
                # Once the strings are assigned to a variable
                # they will be added to our empty lists using the append method
                names.append(full_name)
                birthdates.append(dob)
                # All of this will happen for each iteration 
                # Then once finished, the .txt file will close as
                # we are at the end of the block code


print("Name")   # This is just to print a title before the contents of our list
# We will conduct two for loops to iterate through our lists
# First for loop will iterate through the list of full names stored in names
for list in names:
        print(list)           

print("\n\nBirthdate")  # This is just to print a title before the contents of our list
# First for loop will iterate through the list of DOB's stored in birthdates
for list in birthdates:
        print(list)





