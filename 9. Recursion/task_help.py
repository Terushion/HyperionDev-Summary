
# Example One
print("Example One:")

def walk(steps):
    if steps == 0:
        return
    walk(steps - 1)
    print(f"You take step #{steps}")

walk(11)

# Example Two
print("\nExample Two:")

def count_all(lst):
# Base case.
    if len(lst) == 0:
        return 0
        # Recursive case.
    else:
        return lst[0] + count_all(lst[1:])


sample = [4, 6, 2, 1]
print(count_all(sample))


# Example Three
print("\nExample Three:")

def countdown(n):
    print(n)
    if n == 0:
         return             # Terminate recursion
    else:
         countdown(n - 1)   # Recursive call

countdown(5)

# OR

# def countdown(n):
#     print(n)
#     if n > 0:
#         countdown(n - 1)


