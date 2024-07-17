# award.py

"""
Follow these steps:
● Create a new Python file in this folder called award.py.

● Design a program that determines the award a person competing in a
triathlon will receive.

● Your program should read in the times (in minutes) for all three events of a
triathlon, namely swimming, cycling, and running, and then calculate and
display the total time taken to complete the triathlon.

● The award a participant receives is based on the total time taken to
complete the triathlon. The qualifying time for awards is 100 minutes.
Display the award that the participant will receive based on the following
criteria:

Qualifying criteria                                     Time range                  Award
Within the qualifying time.                             0-100 minutes               Provincial colours
Within five minutes of the qualifying time.             101-105 minutes             Provincial half colours
Within ten minutes of the qualifying time.              106-110 minutes             Provincial scroll
More than ten minutes off from the qualifying time.     111+ minutes                No award

"""

# Program will ask the user to input three integers for the time range in each triathlon event


swimming = int(input("Please input the time taken, in minutes, you finished the Swimming event in: \n"))
print()

cycling = int(input("Please input the time taken, in minutes, you finished the Cycling event in: \n"))
print()

running = int(input("Please input the time taken, in minutes, you finished the Running event in: \n"))
print()

# The sum of all the times for the events

total_time = swimming + cycling + running
print(f"Your total time in the triathlon is {total_time}")
print()

# This will output a different response based on the total time it took the user to comeplete the triathlon
# Each outcome will also state what award the user will recieve if they completed in sufficient timing

if total_time <= 100:
    print("Unbelievable! You performed within the qualifying time so you will be awarded with a Provisional colours award!")

elif total_time > 100 and total_time < 106:
    print("Fantastic job! You performed within 5 minutes of the qualifying time so you will be awarded with a Provisional half colours award!")

elif total_time >= 106 and total_time < 111 :
    print("Amazing! You performed within 10 minutes of the qualifying time so you will be awarded with a Provisional Scroll award.")

else:
    print("Well done for completing the triathlon! Unfortunately, you performed more than 10 minutes off of the qualifying time so you will not receive an award.")

