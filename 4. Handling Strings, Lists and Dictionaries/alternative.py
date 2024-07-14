""" Practical Task One """

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
