import random
import numpy as np
import matplotlib.pyplot as plt

# Generate data
# linspace method loads z-number of datapoints
# at equal intervals between x and y
x = np.linspace(0, 2, 500)

# Set figure size
plt.figure(figsize = (10, 10))

# Plot 3 lines
plt.plot(x, x, label = "linear", linestyle = "--")
plt.plot(x, x**2, label = "quadratic")
plt.plot(x, x**3, label = "cubic", linestyle = ":")

# Show graphic
plt.show()
