""" Practical Task Three"""

"""

Task:

1. Using the following array: [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
Create a Python script called sort_and_search.py.
Which searching algorithm would be appropriate to use on the given list?

2. Implement this search algorithm to search for the number 9. Add a
comment to explain why you think this algorithm was a good choice.
3. Research and implement the Insertion sort on this array.
4. Implement a searching algorithm you haven't tried yet in this Task on the
sorted array to find the number 9. Add a comment to explain where you
would use this algorithm in the real world.

"""

array = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Method for linear search
def linear_search(value, my_list):

    """
    This algorithm is a good choice for searching small lists or unsorted lists. 
    Since it iterates through each element in the list until it finds the desired value,
    it is simple to implement and understand. However, its time complexity is O(n),
    meaning its performance decreases linearly with the size of the list.

    """

    # Iterate over otems until correct value is found
    # Return value otherwise return none if value is not found
    for i in range(len(my_list)):
        if my_list[i] == value:
            return (
                f"The value '{value}' has the index: {i}, in the list 'array'"
                )

print(linear_search(9, array))
print()


# Method for swap, which is encapsulated in the insertion_sort function
def swap(lst, value_1, value_2):
    lst[value_1], lst[value_2] = lst[value_2], lst[value_1]
    return lst

# Method for insertion sort
def insertion_sort(lst):
    for i in range(len(lst)):
        swaps = 0
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                swap(lst, j, j + 1)
                swaps = 1
        if swaps == 0:
            break
    return lst


answer = insertion_sort(array)
print(answer)


# Method for binary search
def binary_search(value, my_list):

    """
    When it comes to comparing large data, it is quite efficient
    as it works on the technique to eliminate half of the array element.
    It has less compilation time and thus better time complexity.
    
    """
    
    low, high = 0, len(my_list)-1
    while high >= low:
        # Get mid point
        mid = (low + high) // 2

        # If value is found at mid point return
        if my_list[mid] == value:
            return mid
        # If value is larger then the mid point value set low
        # to mid selecting the second half of the list
        elif my_list[mid] < value:
            low = mid + 1
        # If value is smaller then the mid point value set low
        # to mid selecting the second half of the list
        else:
            high = mid - 1

print()
print(binary_search(9, answer))