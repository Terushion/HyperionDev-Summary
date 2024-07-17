# Practical Task One

"""
Follow these steps:

    ● Create a file called alternative.py.
    ● Write a program that reads in a string and makes each alternate
    character into an upper case character and each other alternate character
    a lower case character.
    e.g. The string “Hello World” would become “HeLlO WoRlD”
    ● Now, try starting with the same string but making each alternative word
    lower and upper case.
    e.g. The string: “I am learning to code” would become “i AM learning
    TO code”.
    Tip: Using the split() and join() functions will help.

"""

message = "Hello World\n"   # String type Variable
print(message)
message = message.split()   # Splits string into a list of characters
message[0] = "HeLlO"    # Alters first index
message[1] = "WoRlD"    # Alters second idex 
message1 = ' '.join(message) 
# Joins list back into a string under new variable
print(message1)

# Same process is repeated below but not indexes are edited
print()
line = "I am learning to code\n"
print(line)
line = line.split()
line[0] = "i"
line[1] = "AM"
line[3] = "TO"
line1 = ' '.join(line)
print(line1)
