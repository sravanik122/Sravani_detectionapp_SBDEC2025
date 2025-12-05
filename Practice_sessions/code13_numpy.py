import numpy as np

A = np.array([[2, 1], [1, 3]])
B = np.array([8, 18])

X = np.linalg.solve(A, B)

print("Matrix A:\n", A)
print("Vector B:", B)
print("Solution X:", X)