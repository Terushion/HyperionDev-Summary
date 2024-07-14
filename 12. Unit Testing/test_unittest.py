""" Practical Task - Unit Testing """

import unittest


# Taken from Task 14 - Sort & Sorting
# Function taken from sort_and_search

# Method for linear search

array = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

def linear_search(value, my_list):

    # Iterate over otems until correct value is found
    # Return value otherwise return none if value is not found
    for i in range(len(my_list)):
        if my_list[i] == value:
            return (
                f"The value '{value}' has the index: {i}, in the list 'array'"
                )
        else:
            if not isinstance(value, (int, float)):
                return None


"""
Use Case 1: Searching for an existing value in the list.
Use Case 2: Searching for a value that does not exist in the list.
Use Case 3: Searching for non-integer and non-float values.
"""

class TestExamples(unittest.TestCase):

    # Linear search
     def test_linear_search_with_one_value(self):
        lst = [7]
        result = linear_search(7, lst)
        # self.assertEqual(result, 7)
        self.assertTrue(result, True)


     def test_linear_search_with_five_values(self):
        lst = [7, 19, 56, 101, 42]
        result = linear_search(15, lst)
        # self.assertEqual(result, 7)
        self.assertEqual(result, None)


     def test_linear_search_with_string(self):
        lst = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18,]
        result = linear_search("b", lst)
        # self.assertEqual(result, 7)
        self.assertIsNone(result, lst)


     def test_linear_search_with_ten_values(self):
        lst = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18,]
        result = linear_search(-3, lst)
        # self.assertEqual(result, 7)
        self.assertEqual(result, "The value '-3' has the index: 1, in the list 'array'")
