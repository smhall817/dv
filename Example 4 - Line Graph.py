import matplotlib.pyplot as plt
import random

# Generate x and y values
x_values = []
y_values = []
for i in range(10):
    x_values.append(random.randint(1,20))
    y_values.append(random.randint(1,20))
x_values.sort()

# Plot and label figure
plt.plot(x_values, y_values)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Line Graph")

# Show graphic
plt.show()
