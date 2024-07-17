""" Practical Task One """

"""
Follow these steps:

● Create a Python file called holiday.py.
● Your task will be to calculate a user’s total holiday cost, which includes the
plane cost, hotel cost, and car-rental cost.
● First, get the following user inputs:

    ○ city_flight: The city they will be flying to (you can create some
    options for them. Remember each city will have different flight
    costs).
    ○ num_nights: The number of nights they will be staying at a hotel.
    ○ rental_days: The number of days for which they will be hiring a
    car.

● Next, create the following four functions:

    ● hotel_cost(): This function will take num_nights as an argument,
    and return a total cost for the hotel stay (you can choose the price
    per night charged at the hotel).
    ● plane_cost(): This function will take city_flight as an argument
    and return a cost for the flight. Hint: use if/else statements in the
    function to retrieve a price based on the chosen city.
    ● car_rental(): This function will take rental_days as an argument
    and return the total cost of the car rental (you can choose the daily
    rental cost).
    ● holiday_cost(): This function takes three arguments: num_nights,
    city_flight, and rental_days. Using these three arguments, call the
    hotel_cost(), plane_cost(), and car_rental() functions with
    their respective arguments, and finally return the total cost for the
    holiday.

● Print out all the details about the holiday in a readable way.
● Try running your program with different combinations of input to show
its compatibility with different options.
"""

# This a import function, the program will make use of time 
import time

# Functions to calculate the totatl cost for the user's chosen holiday
def hotel_cost(num_nights, a):
    return num_nights * a

def plane_cost(city_flight, a):

    print()    
    if city_flight == "St. George":
        print(f"The price for the flight to St. George is £{a}")
        print()
    elif city_flight == "Kingston":
        print(f"The price for the flight to Kingston is £{a}")
        print()
    elif city_flight == "Montego Bay":
        print(f"The price for the flight to Montego Bay is £{a}")
        print()
    elif city_flight == "Port of Spain":
        print(f"The price for the flight to Port of Spain is £{a}")
        print()

def car_rental(dailyprice, rental_days):
    return rental_days * dailyprice

def holiday_cost(a, b, c):
    total = a + b + c
    print(),
    print(f"Just to confirm, your chosen destination is to {city_flight}, ",
    f"for a total of {num_nights} nights.\n",
    f"This will include your choice to rent a car for {rental_days} days.",
    f"The total price for your desired holiday is £{total}")

# This function will act as a configurator/menu 
def configure():
    print("Here are the available cities to fly to:\n")
    for i in cities_list:
        print(i)

    print()

# All the neccessary variables needed
stgeorge_price = 645
kingston_price = 611.82
montegobay_price = 580.45
portofspain_price = 499.99
hotelprice = 105.30
dailyprice = 25

# A list containing all the city locations
cities_list = ['St. George','Kingston','Montego Bay','Port of Spain']

print()
print("This program will calculate the total cost for your desired holiday.\n")
print()
print("Here are the available cities to fly to:\n")
time.sleep(0.7)

#This will print the list of cities out to show the user their options
for i in cities_list:
    
    print(i)

print()
time.sleep(0.7)
city_flight = ""

# This while loop will gain the user's choice of destination if entered right
# If not, user will be given another chance and so on
# The user can choose to exit the program
while city_flight != "e":
    city_flight = str(input("Which destination would you like to fly to"
                " (Case sensitive): or enter e to cancel and exit\n"))
    if city_flight == "Kingston":
        plane_cost(city_flight, kingston_price)
        break
    elif city_flight == "St. George":
        plane_cost(city_flight, stgeorge_price)
        break
    elif city_flight == "Montego Bay":
        plane_cost(city_flight, montegobay_price)
        break
    elif city_flight == "Port of Spain":
        plane_cost(city_flight, portofspain_price)
        break
    elif city_flight == "e":
        print("Thank you, see you later")
        break
    else:
        print("Unrecognized option. Please Try again")
        configure()

# This while loop will gain the user's other choices
# this is because they didn't exit the program and they entered the destination correctly

while city_flight == "Kingston" or "St. George" or "Montego Bay" or "Port of Spain":

    if city_flight == "e":
        break

    num_nights = int(input("How many nights would you like to stay for"
                            " (e.g. 4 or 9):\n"))
    hotel = hotel_cost(num_nights, hotelprice)
    print()
    print(f"The price of your stay would be £{hotel}.")

    print()
    rental_days = int(input("How many days do you need to hire a rental car"
                            " (e.g. 4 or 9):\n"))
    rental = car_rental(dailyprice, rental_days)
    print(f"The total price to hire a rental would be £{rental}.")

    if city_flight == "Kingston":
        holiday_cost(hotel, kingston_price, rental)
    elif city_flight == "St. George":
        holiday_cost(hotel, stgeorge_price, rental)
    elif city_flight == "Montego Bay":
        holiday_cost(hotel, montegobay_price, rental)
    elif city_flight == "Port of Spain":
        holiday_cost(hotel, portofspain_price, rental)
    break

