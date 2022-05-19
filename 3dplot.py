import numpy as np
import matplotlib.pyplot as plt
PI = np.pi

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x_range = np.linspace(-7, 7, 1000)
y_range = np.linspace(0, 10, 1000)
x, y = np.meshgrid(x_range, y_range)

z = np.sin(x) * np.sin(y)

ax.plot_surface(x, y, z, cmap="summer")
ax.contour(x, y, z, colors="gray", offset=-1)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()
