# Write a NumPy program to convert a list and tuple into arrays.
import numpy as np

my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)

# Convert the list and tuple into arrays
list_array = np.array(my_list)
tuple_array = np.array(my_tuple)

print("Original list:", my_list)
print("Converted array from list:", list_array)

print("\nOriginal tuple:", my_tuple)
print("Converted array from tuple:", tuple_array)
