import random
import matplotlib.pyplot as plt
#import numpy as np

# Generate random data and sort
x_values = [random.randint(1,50) for x in range(100)]
y_values = [random.randint(1,50) for x in range(100)]
x_values.sort()
y_values.sort()

# Create a figure
plt.scatter(x_values, y_values, c = 'green')

# Labels
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Scatter Plot")

# Show graphic
plt.show()
