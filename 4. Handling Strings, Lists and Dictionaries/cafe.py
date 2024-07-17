# Practical Task Two

"""
Follow these steps:

    ● Imagine you are running a café. Create a new Python file in your folder
    called cafe.py.
    ● Create a list called menu, which should contain at least four items sold in
    the café.
    ● Next, create a dictionary called stock, which should contain the stock
    value for each item on your menu.
    ● Create another dictionary called price, which should contain the prices for
    each item on your menu.
    ● Next, calculate the total_stock worth in the café. You will need to
    remember to loop through the appropriate dictionaries and lists to do
    this.
    Tip: When you loop through the menu list, the 'items'can be set as keys to
    access the corresponding 'stock' and 'price' values. Each 'item_value' is
    calculated by multiplying the stock value by the price value. For example:
    item_value = (stock[items] * price[items])
    ● Finally, print out the result of your calculation
"""

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
