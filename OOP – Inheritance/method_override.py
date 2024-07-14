"""     Practical Task Two      """

# Take user inputs that ask for the name, age, hair colour, and eye colour of a
# person.
# ● Create an Adult class with the following attributes and method:
# ○ Attributes: name, age, eye_colour, and hair_colour
# ○ A method called can_drive() which prints the name of the person
# and that they are old enough to drive.
# ● Create a subclass of the Adult class named Child that has the same
# attributes, but overrides the can_drive() method to print the person's name
# and that they are too young to drive.
# ● Create some logic that determines if the person is 18 or older and create an
# instance of the Adult class if this is true. Otherwise, create an instance of the
# Child class. Once the object has been created, call the can_drive() method
# to print out whether the person is old enough to drive or not.

# Parent class for an adult which we can extend to a subclass
class Adult:

    # Constructor that allows us to set the characteristics
    # as instance variables
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self) -> str:
        return f"{self.name} is {self.age} years old and is old enough to drive."


class Child(Adult):  # Child inherits from Adult

    def cant_drive(self) -> str:
        return f"{self.name} is {self.age} years old and is too young to drive."

# Variable List
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
hair_colour = input("What is your hair colour: ")
eye_colour = input("What is the colour of your eyes: ")

# If-Else statement to determine whether user can drive or not
if age >= 18:
    senior = Adult(name, age, hair_colour, eye_colour)
    print(senior.can_drive())
else:
    minor = Child(name, age, hair_colour, eye_colour)
    print(minor.cant_drive())
