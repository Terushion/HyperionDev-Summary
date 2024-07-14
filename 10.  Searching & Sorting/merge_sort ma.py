"""Practical Task 2 model answers"""


def merge_sort_by_length(arr):
    """
    Args: The chosen list of strings
    Return: A sorted list of strings by string length.
    """
    # Base case - ends the program if there is 1 or fewer elements in the list
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort_by_length(left_half)
    right_half = merge_sort_by_length(right_half)

    # Merge the sorted halves
    return merge_by_length(left_half, right_half)


def merge_by_length(left, right):
    """
    Args: The left-halve's sorted list of strings and the right-halve's sorted list of strings.
    Return: The merged sorted list of strings.
    """
    result = []
    # While both lists have elements, compare and append the longer one
    while left and right:
        if len(left[0]) >= len(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result + left + right


# Define 3 lists containing 10 strings of different lengths
list1 = ["apple", "banana", "grapefruit", "kiwi", "orange", "watermelon",
         "strawberry", "peach", "pineapple", "blueberry"]

list2 = ["python", "rust", "java", "javascript", "c", "c++", "ruby", "react",
         "go", "typescript"]

list3 = ["elephant", "lion", "tiger", "giraffe", "zebra", "rhinoceros",
         "hippo", "cheetah", "kangaroo", "crocodile"]

# Test the modified Merge sort algorithm with the lists
print("Sorted list 1:", merge_sort_by_length(list1))
print("Sorted list 2:", merge_sort_by_length(list2))
print("Sorted list 3:", merge_sort_by_length(list3))
