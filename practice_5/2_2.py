import numpy as np
import matplotlib.pyplot as plt

result = []
for i in range(10):
    x = np.random.rand(10)
    result.append(sum(x))
num_bins = 10
n, bins, patches = plt.hist(result, num_bins)
plt.xlabel('result')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()