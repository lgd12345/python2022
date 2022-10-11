import numpy as np
import matplotlib.pyplot as plt

points = np.array([
    [1, 1], [1, 2], [1, 3],
    [2, 1], [2, 2], [2, 3],
    [3, 1], [3, 2], [3, 3]
])
print(points)
plt.plot(points[:, 0], points[:, 1], "ro")  # r : red, o: circle
# plt.show()

# bar막대그래프
plt.bar(points[:, 0], points[:, 1])


p = np.array([2.5, 2])
plt.plot(p[0], p[1], "bo")  # b : blue, o : oircle

plt.show()
