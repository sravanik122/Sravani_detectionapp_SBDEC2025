import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vertical Stack:\n", np.vstack((a, b)))
print("Horizontal Stack:\n", np.hstack((a, b)))

arr = np.arange(10)
split = np.array_split(arr, 3)
print("Splitted Arrays:", split)