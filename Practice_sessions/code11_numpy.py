import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
vector = np.array([10, 20, 30])

print("After Broadcasting:\n", arr + vector)