import numpy as np

# the number of values in a set
b = np.zeros(2, dtype=int)
print("Matrix b : \n", b)

# index 0 is the number of values and index 1 is the number of sets
a = np.empty([2, 2], dtype=int)  # row x column
print("\nMatrix a : \n", a)

c = np.empty([3, 3])
print("\nMatrix c: \n", c)

a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# adding values of different sets with the same index
add_ans = a+b
print(add_ans)

add_ans = np.add(a, b)
print(add_ans)

# subtracting values of different sets with the same index
sub_ans = a-b
print(sub_ans)

sub_ans = np.subtract(a, b)
print(sub_ans)

# multiplying values of different sets with the same index
mul_ans = a*b
print(mul_ans)

mul_ans = np.multiply(a, b)
print(mul_ans)

# dividing values of different sets with the same index
div_ans = a/b
print(div_ans)

div_ans = np.divide(a, b)
print(div_ans)