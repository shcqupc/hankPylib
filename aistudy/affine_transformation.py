import numpy as np
import matplotlib.pyplot as plt
x = np.random.random([10000, 2])
print(x.shape)
#A = np.array([[2, 0], [0, 1]])
A = np.array([[np.cos(np.pi/3)*2, np.sin(np.pi/3)], [-np.sin(np.pi/3), np.cos(np.pi/3)*2]])
print(A)
y = np.dot(x, A)
print(y.shape)
plt.scatter(x[:, 0], x[:, 1], c='r',alpha=1,marker='.')
plt.scatter(y[:, 0], y[:, 1], c='b',alpha=0.2,marker='.')
plt.axis("equal")
plt.show()
