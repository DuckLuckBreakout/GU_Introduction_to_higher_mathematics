import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 400)
y = [5]*400

plt.polar(x, y)
plt.show()