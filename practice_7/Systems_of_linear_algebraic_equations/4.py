import numpy as np
import scipy
import scipy.linalg

A = np.array([[1, 2, 3],
              [2, 16, 21],
              [4, 28, 73]])


P, L, U = scipy.linalg.lu(A)

B = np.array([4, 1, 7])
print(np.linalg.solve(A, B))