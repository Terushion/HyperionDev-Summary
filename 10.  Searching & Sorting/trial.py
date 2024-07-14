def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if len(left[left_index]) >= len(right[right_index]):
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

lists = [
    ["apple", "banana", "orange", "kiwi", "grape", "strawberry", "blueberry", "raspberry", "pineapple", "pear"],
    ["elephant", "giraffe", "hippopotamus", "rhinoceros", "lion", "tiger", "zebra", "cheetah", "elephant", "gazelle"],
    ["python", "java", "javascript", "ruby", "c", "c++", "swift", "php", "rust", "perl"]
]

for i, lst in enumerate(lists):
    print(f"Original list {i + 1}: {lst}")
    sorted_list = merge_sort(lst)
    print(f"Sorted list {i + 1}: {sorted_list}\n")
