import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z1 = 2*X - 5*Y
ax.plot_wireframe(X, Y, Z1)
Z2 = 2*X - 5*Y + 20
ax.plot_wireframe(X, Y, Z2, color='green')
show()