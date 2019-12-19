import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3*np.pi, 3*np.pi, 201)

a = 5
b = 2
k = 1
plt.plot(x, k*np.cos(x - a) + b, color='red')
a = -2
b = 0
k = 7
plt.plot(x, k*np.cos(x - a) + b, color='blue')
a = 0
b = -10
k = 3
plt.plot(x, k*np.cos(x - a) + b, color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.show()
