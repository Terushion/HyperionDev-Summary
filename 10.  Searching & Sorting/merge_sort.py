""" Practical Task Two"""

"""

1. Modify the Merge sort algorithm to order a list of strings by string length
from the longest to the shortest string.

2. Run the modified Merge sort algorithm against 3 string lists of your
choice. Please ensure that each of your chosen lists is not sorted and has a
length of at least 10 string elements.

"""


# Method for merge_sort function
def merge_sort(arr):
    if len(arr) > 1:
    
      mid = len(arr) // 2
      left_arr = arr[:mid]
      right_arr = arr[mid:]

      # Recursion 
      merge_sort(left_arr)
      merge_sort(right_arr)
      

      # Merge
      i = 0   # Left array index
      j = 0   # Right array index
      k = 0   # Merged array index


      while i < len(left_arr) and j < len(right_arr):
          # Comaprison between left and right array 
          if left_arr[i] < right_arr[j]:
              arr[k] = left_arr[i]
              # If the left_arr[i] is less, then the first index in the list
              # will be left_arr[i]
              i += 1
              
          else:
              arr[k] = right_arr[j]
              j += 1
          k += 1 
          # No matter what, the index 'k' will increment by 1 
              
      # These while loops below will be incase, all the elements are transferred
      # to the merged array meaning the remaining array has nothing to compare to

      while i < len(left_arr):
          arr[k] = left_arr[i]
          i += 1
          k += 1


      while j < len(right_arr):
          arr[k] = right_arr[j]
          j += 1
          k += 1
    
    return arr



# First list
fruits = [
    "Dragonfruit", "Passionfruit", "Lychee", "Mango",
    "Papaya", "Guava", "Starfruit", "Strawberry",
    "Grape", "Watermelon"
]


# Second list
colors = [
    "Cerulean", "Teal", "Green", "Yellow",
    "Merigold", "Orange", "Violet", "White",
    "Coral", "Lime"
]


# Third list
animals = [
    "African Elephant", "Giraffe", "Lion", "Sumatran Tiger",
    "Zebra", "Hippopotamus", "Rhinoceros", "Silverback Gorilla",
    "Sea Turtle", "Black Panther", "Mandrill", 
]


# Sorting each list
sorted_fruits = merge_sort(fruits)
sorted_colors = merge_sort(colors)
sorted_animals = merge_sort(animals)


# Printing the sorted lists
print(f"Sorted Fruits: {sorted_fruits}")
print()
print(f"Sorted Colors: {sorted_colors}")
print()
print(f"Sorted Animals: {sorted_animals}")


print()


