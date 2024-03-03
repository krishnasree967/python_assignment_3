# Write a Python program to reverse the order of the items in the array.

from array import array
original_array = array('i', [1, 3, 5, 7, 9])

original_array.append(11)

print(f"New array: {original_array}")