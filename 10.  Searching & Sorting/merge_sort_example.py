"""
Merge Sort
Like QuickSort, Merge Sort is also a 'divide and conquer' strategy. In this strategy,
we break apart the list to then put it back together in order. To start, we break the
list into two and keep dividing until each element is on its own. Next, we start
combining them two at a time and sorting as we go. Have a look at the example
below. We start by dividing up the elements:

"""

# Method for merge_sort function
def merge_sort(arr):
    if len(arr) > 1:
      
      mid = len(arr) // 2
      left_arr = arr[:mid]
      right_arr = arr[mid:]

      # Recursion 
      merge_sort(left_arr)
      merge_sort(left_arr)

      # Merge
      # Initial values for pointers that we use to keep track,
      # of where we are in each array
      i = 0   # Left array index
      j = 0   # Right array index
      k = 0   # Merged array index

      # Until we reach the end of either start or end, pick larger among
      # elements start and end and place them in the correct position in the sorted array
      while i < len(left_arr) and j < len(right_arr):
          if left_arr[i] < right_arr[j]:
              arr[k] = left_arr[i]
              i += 1
              
          else:
              arr[k] = right_arr[j]
              j += 1
          k += 1  
              
      # When all elements are traversed in either left_arr or right_arr,
      # pick up the remaining elements and put in sorted array
      while i < len(left_arr):
          arr[k] = left_arr[i]
          i += 1
          k += 1

      while j < len(right_arr):
          arr[k] = right_arr[j]
          j += 1
          k += 1
    
    return arr
    
arr_test = [54, 26, 93, 17, 77, 31, 44, 55, 20, 4, 2, 1, 9, 5, 16]

print(arr_test)

merge_sort(arr_test)
print(f"\n{arr_test}")



