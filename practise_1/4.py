import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3*np.pi, 3*np.pi, 201)

k = 1
plt.plot(x, np.cos(k*x))
k = 2
plt.plot(x, np.cos(k*x))
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.show()