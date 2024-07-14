""" Practical Task Two"""

""" 
create a function that returns the
largest number in a list of integers taken as an argument. The problem
needs to be solved recursively without using loops.
Examples of input and output:
largest_number([1, 4, 5, 3])
=> 5
largest_number([3, 1, 6, 8, 2, 4, 5]


I want to compare the first element in the list to the second one,
to check which element is the largest number.
Then I want to wrtie some logic that focuses on the largest element
out of the two whilst maybe putting the old one aside or deleting it.
The function will call itself and will only stop once there's logic 
that stops it either by only having one element in the list or when 
there are no more indexes whilst the largest element has been saved
under a variable that can be returned to the user in the terminal

"""

""" What I essentially want to do but recursively """

# def largest_num():

#     list = [5, 66, 14, 31, 5, 9, 11, 17, 2, 31, 46, 21, 112, 79]

#     list.sort( reverse=True)
#     # re-arranges the list above
#     # But in the parameters reverse=True
#     #This means the list will be sorted in reverse from highest to lowest
#     return list[0]

# print(largest_num())

def largest_num(lst, largest=0):
    # Base case:
    if len(lst) == 0:
        return "None", "\nList is empty"
    # if the length of the list is 0, then return the string above
    elif len(lst) == 1:
        return f"The largest number in the list is {lst[0]}"
    # when the length of the list is finally one, which will be the 
    # number that is largest in the list, the string above,
    # and that number will be returned to user in the termimal

    # Recursive case: return the value that resides in the first index '[0]'
    elif lst[0] > lst[1]:
        largest = lst[0]
        lst.pop(1)
        return largest_num(lst, largest)
    else:
        lst[1] > lst[0]
        largest = lst[1]
        lst.pop(0)
        return largest_num(lst, largest)
    # else:
    #      return largest


list = [5, 66, 14, 31, 5, 9, 11, 17, 2, 31, 46, 21, 112, 79]
print(largest_num(list))

