"""
Task: 
------------------
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""

# Parent/Base Class
class Course:
    # Class Variables
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    # Method for contact details
    def contact_details(self):
        return f"Please contact us by visiting", self.contact_website

    # Method for Head Office Location
    def head_office(self, location= "Cape Town"):
        self. location = location
        return f"The Head Office Location is: {self.location}."

# Child/Sub Class    
class OOPCourse(Course):

    # Constructor that allows us to set the characteristics
    # as instance variables
    def __init__(self, description="OOP Fundamentals", trainer= "Mr Anon A. Mouse"):
        self.description = description
        self.trainer = trainer
        self.course_id = "12345"

    # Method for trainer details
    def trainer_details(self) -> str:
        return (f"The course: {self.description}"
        f"is about the basic fundamentals of object-oriented programming (OOP).\n"
        f"The trainer that will teach this topic is {self.trainer}.\n")
    
    # Method for returning all neccessary information
    def course_1(self) -> str:
        return (f"Contact details: {self.contact_website}\n"
        f"\nTrainer: {self.trainer}"
        f"\nCourse ID: {self.course_id}")

# Using variable to access class functions        
my_course = OOPCourse()

# Print statements
print(my_course.head_office())
print(my_course.course_1())
print(my_course.trainer_details())

