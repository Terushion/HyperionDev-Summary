""" Practical Task 2 """

# We need one variable that will be able to record the number
# of students that need to register
# We need two others that will record the ID's of the students
# Whilst the other record the former as a list or for our .txt file 
id_num = 0
reg_form = ""
num_students = int(input("Please enter the number of students "
                         "that are registering: \n"))
print()
       
try:
    for i in range(1, num_students + 1):    # using for loop to obtain our values
        if i != (num_students + 1):
            id_num = (input("Please enter your student ID number: \n"))
            reg_form += id_num + "..\n"
            print()
except ValueError as e:
        print(f"Error: {e}, "
              "This was an invalid input, next time, enter a number please")     
        
# If i doesn't equal to the max number in range, the program
# will ask user to input the ID numbers of students who are present
# Once this is completed they will be recorded in 'reg_form'
# That will serve as a register for the exam venue
# However, if the user makes a mistake and enters anything but an integer
# the exception will be executed with the error in question

print(reg_form)     # This is to show what has been recorded
with open('reg_form.txt', 'a') as file:
     
     file.write(f"{reg_form}\n")

# This with/as open function will create the file reg_form if,
# it hasn't already
# The next line of code will append the contents of the variable,
# reg_form to our text file and will close once the block of code,
# has been executed.

# ************ Another Example ************

# This will save all the student ID numbers in a list

# reg_form = []
       
# try:
#     for i in range(1, num_students + 1):
#         if i != (num_students + 1):
#             id_num = (input("Please enter your student ID number: \n"))
#             reg_form.(id_num + "..\n")
#             print()
# except ValueError as e:
#         print(f"Error: {e}, "
#               "This was an invalid input, please enter a number")     
                     
# print(reg_form)
# with open('reg_form', 'a') as file:
    #  for line in reg_form:
    #       file.write(f"\n{reg_form}")