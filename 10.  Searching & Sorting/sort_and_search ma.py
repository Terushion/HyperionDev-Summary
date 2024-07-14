"""Practical Task 3 model answers"""

# On the given list, the linear search algorithm is the best option to find the target number
# because the list is unsorted. The binary search algorithm would have been the better option
# if the given list was sorted.


def linear_search(arr, target):
    """
    Arguments: The list of integers and the target number to find
    Return: The index of the target number if found, otherwise -1
    """
    for index, value in enumerate(arr):
        if value == target:
            # Return the index if the target is found
            return index
    # Return -1 if the target is not found
    return -1


def insertion_sort(arr):
    """
    Sorts the list of integers in ascending order

    Argument: The list of integers to sort
    Return: No return value, it simply modifies the array of integers
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def binary_search(arr, target):
    """
    Arguments: The list of integers and the target number to find
    Return: The index of the target number if found, otherwise -1
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


array = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
TARGET_NUMBER = 9

# Linear search section
print("Unsorted array:", array)
linear_index = linear_search(array, TARGET_NUMBER)

if linear_index != -1:
    print(f"The number {TARGET_NUMBER} was found at index {linear_index} using linear search.")
else:
    print(f"The number {TARGET_NUMBER} was not found using linear search.")

# Binary search section
insertion_sort(array)
print("\nSorted array:", array)
binary_index = binary_search(array, TARGET_NUMBER)

if binary_index != -1:
    print(f"The number {TARGET_NUMBER} was found at index {binary_index} using binary search.")
else:
    print(f"The number {TARGET_NUMBER} was not found using binary search.")


# The binary search algorithm would be best utilized in real-world scenarios where data is already
# sorted. An example of this would be searching for a word in a dictionary. Instead of starting from
# the first page, you can start from the middle and then decide whether to page back or forward
# based on the word you are searching for.
