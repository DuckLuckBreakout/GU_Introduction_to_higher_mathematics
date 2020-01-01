import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# 0 решений
# B = np.array([[12, 2, 1]])

# Бесконечное число решений
B = np.array([[88, 92, 96]])

C = np.concatenate((A, B.T), axis=1)
if np.linalg.matrix_rank(A, 0.0001) < np.linalg.matrix_rank(C, 0.0001):
    print("Не имеет решений")
elif np.linalg.matrix_rank(A, 0.0001) == np.linalg.matrix_rank(C, 0.0001):
    if np.linalg.matrix_rank(A, 0.0001) < len(A[0]):
        print("Бесконечное число решений")
    else:
        print("Единственное решение")
