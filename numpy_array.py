# Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.
import numpy as np

# Create arrays
zeros_array = np.zeros(10, dtype=int)  # Array of 10 zeros
ones_array = np.ones(10, dtype=int)    # Array of 10 ones
fives_array = np.full(10, 5, dtype=int)  # Array of 10 fives

# Display arrays
print("Array of 10 zeros:", zeros_array)
print("Array of 10 ones:", ones_array)
print("Array of 10 fives:", fives_array)
