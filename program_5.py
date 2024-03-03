# Write a Python program to find the first duplicate element in a given array of integers. Return -1 if there are no such elements.

def find_first_duplicate(array):
    array.sort()
    for j in range(len(array) - 1):
        if array[j] == array[j + 1]:
            return array[j]
    return -1


print(find_first_duplicate([1, 2, 3, 4, 4, 5])) 
print(find_first_duplicate([1, 2, 3, 4, 5]))     
print(find_first_duplicate([1, 1, 2, 3, 4, 5])) 