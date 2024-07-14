""" Practical Task Two """

# List of menu 

menu = ['Chai Latte', 'Peppermint Tea', 'Hot Chocolate', 'Tropical Smoothie'] 

# Dictionaries

# Dictionary of stock
stock = {
    "Chai Latte": 8,
    "Peppermint Tea": 13,
    "Hot Chocolate": 20,
    "Tropical Smoothie": 10
}

# Dictionary of price
price = {
    "Chai Latte": 4.50,
    "Peppermint Tea": 1.95,
    "Hot Chocolate": 3.20,
    "Tropical Smoothie": 6
}

# Using values of the dictionaries to calculate stock worth
chai_value = round((stock["Chai Latte"] * price["Chai Latte"]),2)
ptea_value = round((stock["Peppermint Tea"] * price["Peppermint Tea"]),2)
hotc_value = round((stock["Hot Chocolate"] * price["Hot Chocolate"]),2)
tropicals_value = round((stock["Tropical Smoothie"] * price["Tropical Smoothie"]),2)
total_stock = (chai_value + ptea_value +
                  hotc_value + tropicals_value)

# for loop
# Program will run through each item in 'menu' list
# For each item on the list, the program will print out stock worth
# Total stock worth will be printed
for items in menu:
    if items == "Chai Latte":
        print(f"total stock of {items} is worth: £{chai_value}" )
    elif items == "Peppermint Tea":
        print(f"total stock of {items} is worth: £{ptea_value}" )
    elif items == "Hot Chocolate":
        print(f"total stock of {items} is worth: £{hotc_value}" )
    elif items == "Tropical Smoothie":
        print(f"total stock of {items} is worth: £{tropicals_value}\n" )
        print(f"The total of the stock in the cafe is worth",
                f"£{total_stock}")
    else:
        break
