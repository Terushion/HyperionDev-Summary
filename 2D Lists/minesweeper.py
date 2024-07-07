""" Practical Task """


"""
Let's create an example of a multidimensional list representing a game 'Minesweeper'
In this game, the multidimensional list will from a grid full of mines and mine-free spots
Each hash (#) represents amine and each dash (-) represents a mine-free spot in this 2D list.

We'll consider the grid to be of even rows and columns, 
and we'll return the grid
We have to also include functionality to check where the mines are,
and to add a function that ,
where each dash is replaced by a digit, indicating the number of
mines immediately adjacent to the spot i.e. horizontally, vertically, and diagonally.

Example of my extpectation:


input = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]


output =    [   
            ["1", "1", "2", "#", "#"],
            ["1", "#", "3", "3", "2"],
            ["2", "4", "#", "2", "0"],
            ["1", "#", "#", "2", "0"],
            ["1", "2", "2", "1", "0"] 
            ]

"""



def convert(grid):

    """
    This function will convert a list of '#' and '-',
    to represent the game 'Minesweeper'
    This will happen by running a set of for loops
    The first will iterate through the list changing each '-' to 0
    We want to add 1 to an element if there are any adjacent mines
    Which is why we set all mine-free spots to 0,
    as you cannot add an integer to a string
    The next for loops after that will have slightly different ranges,
    as we don't want to have an 'index out of range' error,
    when we iterate through an element whilst checking all the adjacent ones

    E.g. the for loops will check
    if there any mines adjacent to the left or right of grid[1][1],
    as well as ones in the same column but in the row above, and below.
    Then another loop will check diagonally in all four directions
    NW, NE, SW AND SE. 
    if grid[1][1] = 0, then for each mine found surrounding it,
    the integer 1 will be added. 
    if grid[1][1] = # (mine), the logic in the for loops will ensure that,
    it just continues to the next element in the list.
    """

    print("\nMinesweeper:\n")

    rows = len(grid)

    # For loop which will set any mine-free spots to 0 
    for row in range(rows):
        cols = len(grid[row])  # outer loop for rows
        for col in range(cols):  # inner loop for columns
            if grid[row][col] != "#":
                grid[row][col] = 0


    # For loop to check E and NE
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "#":
                continue
            if col < cols - 1 and grid[row][col + 1] == "#":
                grid[row][col] += 1
            if row > 0 and col < cols - 1 and grid[row - 1][col + 1] == "#":
                grid[row][col] += 1
    # 'col < cols - 1' ensures we don't check beyond the rightmost column.
    # 'row > 0 ensures' we don't check above the top row.
    # 'row > 0 and col < cols - 1' ensures we don't check diagonally beyond the grid limits.


    # For loop to check S and SW
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "#":
                continue
            if row < rows - 1 and grid[row + 1][col] == "#":
                grid[row][col] += 1
            if row < rows - 1 and col > 0 and grid[row + 1][col - 1] == "#":
                grid[row][col] += 1
    # 'row < rows - 1' ensures we don't check beyond the bottom row.
    # 'col > 0' ensures we don't check left of the leftmost column.
    # 'row < rows - 1 and col > 0' ensures we don't check diagonally beyond the grid limits.
        

    # For loop to check SE
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "#":
                continue
            if row < rows - 1 and col < cols - 1 and grid[row + 1][col + 1] == "#":
                grid[row][col] += 1
    # 'row < rows - 1 and col < cols - 1' ensures we don't check diagonally beyond the grid limits (bottom-right).

    # For loop to check N, W and NW
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "#":
                continue
            if row > 0 and grid[row - 1][col] == "#":
                grid[row][col] += 1
            if col > 0 and grid[row][col - 1] == "#":
                grid[row][col] += 1
            if row > 0 and col > 0 and grid[row - 1][col - 1] == "#":
                grid[row][col] += 1
    # 'row > 0' ensures we don't check above the top row.
    # 'col > 0' ensures we don't check left of the leftmost column.
    # 'row > 0 and col > 0' ensures we don't check diagonally beyond the grid limits (top-left).


    # This last loop will print the expected outcome in the terminal              
    for row in grid:  # outer loop for rows
        for col in row:  # inner loop for columns
            print(col, end="  ")
        print()

    print()       


minesweeper = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

test_grid_one = [
    ["-", "-", "#", "-", "#"],
    ["-", "#", "-", "-", "-"],
    ["#", "-", "#", "-", "-"],
    ["-", "-", "-", "-", "#"],
    ["#", "-", "-", "-", "-"]
]

test_grid_two = [
    ["-", "-", "-", "-", "#"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "-", "#", "-"]
]

convert(test_grid_one)
convert(test_grid_two)
convert(minesweeper)
