import numpy as np
from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return y - x**2 + 1, np.exp(x) + x*(1 - y) - 1

result = []
for i in range(-10, 10):
    x1, y1 = fsolve(equations, (i, i))
    x1 = round(x1, 6)
    y1 = round(y1, 6)
    if (x1, y1) not in result:
        result.append((x1, y1))
print(result)