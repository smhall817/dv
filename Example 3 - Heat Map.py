import numpy as np
import matplotlib.pyplot as plt

# Generate data using numpy.random.random
# This method creates an array of size x, y,
# containing random floats between 0 and 1
x = np.random.random((40, 40))
x.sort()
print(x)

# Create graphic
# "Autumn" is the color scheme, interpolation is how the
# data points "blend" together
plt.imshow(x, cmap = "autumn", interpolation = "none")

# Add labels
plt.title("Example Heat Map")

# Show graphic
plt.show()
