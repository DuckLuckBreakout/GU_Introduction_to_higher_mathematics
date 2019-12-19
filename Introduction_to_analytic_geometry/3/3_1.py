import numpy as np
import matplotlib.pyplot as plt
import math

x = []
y1 = []
y2 = []
r = 2
x_ = -r
while x_ <= r:
    x_ = round(x_, 2)
    print(x_)
    x.append(x_)
    y1.append(math.sqrt(r**2 - x_**2))
    y2.append(-math.sqrt(r**2 - x_**2))
    x_ += 0.01

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()