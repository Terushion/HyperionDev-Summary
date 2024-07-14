''' Practical task two '''

# Below is our string type variable containing a star

stars = "*" 

"""

To complete the pattern which consists of nine lines
the for loop needs to complete nine iterations for the pattern

"""


for i in range (9):
    print(stars)
    stars = stars + "*"
    if i > 3:
        stars = stars[:-2]
        # Once the index is greater than 3, for each iteration onwards,
        # The program will add one * but then subtract 2 which means
        # Index gets SMALLER as the loop goes on
    else:
        if i == 8:
            break

# Break is used to end the code once the pattern is complete 