import numpy as np

macros = np.array([
    [0.8, 2.9, 3.9],
    [52.4, 23.6, 36.5],
    [55.2, 31.7, 23.9],
    [14.4, 11, 4.9]
])

# Create an empty array of the same size

result = np.zeros_like(macros)

cal_per_macro = np.array([3, 3, 8])

# Method 1
result = np.add(result, cal_per_macro)
total = np.multiply(result, macros)  # First comes the values you're multiplying with
print("\n Method 1 = ", total)

# Method 2
for i in range(macros.shape[0]):  # For i in every row
    result[i, :] = macros[i, :] * cal_per_macro

print("\n Method 2 = ", result)

# Method 3 (Easiest)
total = np.multiply(cal_per_macro, macros)  # First comes the values you're multiplying with
print("\n Method 3 = ", total)

# Broadcasting rules
# 1) Same shape row x column
# 2) Every must either have a 1 or must match the number
# 3) If the shape is shorter, prepend 1 to make them the same length
# (2,) meaning 1 row 2 columns

# Example
# x.shape == (2, 3)
#
# y.shape == (2, 3) compatible
# y.shape == (2, 1) compatible
# y.shape == (1, 3) compatible
# y.shape == (3,) compatible
#
# results in (2, 3) shape
#
# y.shape == (3, 2) NOT compatible
# y.shape == (2,) NOT compatible


# (3, 3)
x = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]])

# (1, 3)
y = np.array([1, 10, 100])

print("\n For (3,3) + (1, 3)= \n", x + y)

z = np.array([[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]])

# (3, 1)
u = np.array([1, 10, 100]).reshape(3, 1)  # Why reshape?

print("\n For (3,3) + (3, 1)= \n", z + u)

shape = (3, 3)
out = np.empty(shape, dtype=int)
N0, N1 = shape

for i in range(N0):
    for j in range(N1):
        out[i, j] = x[i, j] + y[j]  # y[j] == y[0, j]
print("\n For (3,3) + (1, 3)= \n", out)

for i in range(N0):
    for j in range(N1):
        out[i, j] = z[i, j] + u[i, 0]  # plug in 0 for 1
print("\n For (3,3) + (3, 1)= \n", out)

# Practice
v = np.array([12, 24, 36]).reshape(3, 1)  # shape (1, 3) -> (3,1)
w = np.array([45, 55])  # shape (1, 2)

out = np.multiply(v, w)
print(out)

x = np.array([[12, 22, 33], [45, 55, 66]])  # Shape (2, 3)
v = np.array([12, 24, 36])  # Shape (3,)

print(x + v)

# Reverse (Results in different shape with same values)
# v = np.array([12, 24, 36])  # shape (1, 3)
# w = np.array([45, 55]).reshape(2, 1)  # shape (1, 2) -> (2, 1)
#
# out = np.multiply(v, w)
# print(out)

# X = (2, 3) and w = (2,)
# Transpose X to (3, 2) so the shapes are compatible
# Shape result is (3, 2)
# Transpose resulting shape to (2, 3)
# Reshaping means to transform the matrix into whatever shape we wish
# Transposing means to switch the col to row or row to col
print((x.T + w).T)

# Reshape w to be a col
# Gives the same result as transposing

w = np.reshape(w, (2, 1))
print(x + w)

# Multiply/Scale x by a constant

print(x * 2)