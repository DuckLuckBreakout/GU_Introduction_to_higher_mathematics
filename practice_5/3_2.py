import numpy as np
from math import factorial

def c_n_k(n, k):
    return factorial(n)/(factorial(k)*factorial(n - k))

def p_n_k(n, k, p, q):
    return c_n_k(n, k) * p**k * q**(n - k)

k, n = 0, 100000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
e = np.random.randint(0, 2, n)
f = np.random.randint(0, 2, n)
g = np.random.randint(0, 2, n)
x = a + b + c + d + e + f + g
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
#print(a, b, c, d)
#print(x)
print(k, n, k/n)
print(p_n_k(7, 2, 1/2, 1/2))