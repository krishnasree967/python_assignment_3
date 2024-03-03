# Write a Python program to get the number of occurrences of a specified element in an array.

from array import array

original_array = array('i', [1, 3, 5, 3, 7, 9, 3])

occurrence = original_array.count(3)

print(f"Number of occurrences of the number 3 in the said array is: {occurrence}")