import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 1, 100)
y = x * np.sin(25 * x)
z = x * np.sin(25 * x)

# Create figure
fig = plt.figure()

# Create axes and set 3D
ax = plt.axes(projection = "3d")

# Plot data
ax.plot3D(x, y, z, "green")

# Title
ax.set_title("3D Line Graph")

# Show figure
fig.show()
