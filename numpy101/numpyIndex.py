import numpy as np

# Create a sequence of int from 10 to 1 with a step of -2

a = np.arange(10, 1, -2)  # start, stop, step
print("\n A sequential array with a negative step: \n", a)

# Print the value by index

newarr = a[np.array([3, 2, 1])]
print("\n Elements at these indices are:\n", newarr)

# Arrange elements 0 to 19

a = np.arange(20)  # Print all values before 20
print("\n Array is:\n", a)
print("\n a[-8:17:1]= ", a[-8:17:1])  # Why does 17 not count? Because the sequence stops before the stop value
print("\n a[10:]", a[10:])  # Print all values from 10 until the end fo the sequence

b = np.array([[[1, 2, 3], [4, 5, 6]],
              [[7, 8, 9], [10, 11, 12]]])

# Determine the index of the arrays within the brackets and then the values
print("\n A value in the arrays: ", b[1, 0, 2])  # Equivalent to b[: ,: ,1] Taking 1st index of all col and row
print("\n Middle value in all arrays: ", b[..., 1])
print("\n First value in first 2 arrays: ", b[0, :, 0])
print("\n First value in first arrays of both major arrays: ", b[:, 0, 0])