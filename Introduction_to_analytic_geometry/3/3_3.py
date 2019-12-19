import numpy as np
import matplotlib.pyplot as plt
import math

x1 = []
x2 = []
y1_1 = []
y1_2 = []
y2_1 = []
y2_2 = []
a = 2
b = 5
x_ = -a**2
while x_ <= -a + 0.01/2:
    x_ = round(x_, 2)
    print(x_)
    x1.append(x_)
    y1_1.append(math.sqrt(b**2/a**2 * x_**2 - b**2))
    y1_2.append(-math.sqrt(b**2/a**2 * x_**2 - b**2))
    x_ += 0.01

x_ = a
while x_ <= a**2 + 0.01/2:
    x_ = round(x_, 2)
    print(x_)
    x2.append(x_)
    y2_1.append(math.sqrt(b**2/a**2 * x_**2 - b**2))
    y2_2.append(-math.sqrt(b**2/a**2 * x_**2 - b**2))
    x_ += 0.01

plt.plot(x1, y1_1)
plt.plot(x1, y1_2)
plt.plot(x2, y2_1)
plt.plot(x2, y2_2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()