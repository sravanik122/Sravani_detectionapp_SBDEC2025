import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("Sum (axis=0):", np.sum(matrix, axis=0))
print("Sum (axis=1):", np.sum(matrix, axis=1))
print("Mean (axis=0):", np.mean(matrix, axis=0))
print("Cumulative Sum:", np.cumsum(matrix))