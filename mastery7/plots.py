import numpy as np
import matplotlib.pyplot as plt

a = [[1, 1], [1, 1]]
b = [[1, 2, 0, 4, 5, 10], [5, 3, 2, 8, 9, 1]]

out = np.dot(a, b)
plt.scatter(out[0], out[1])
plt.show()