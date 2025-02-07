import numpy as np
import matplotlib.pyplot as plt

# Data
square_footage = np.array([1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
selling_prices = np.array([250, 290, 315, 380, 410, 450, 500, 525, 570, 610])

# Plot
plt.figure(figsize=(8,5))
plt.scatter(square_footage, selling_prices, color='b', marker='o')
plt.xlabel("Square Footage")
plt.ylabel("Selling Price (in $1000s)")
plt.title("House Size vs. Selling Price")
plt.grid(True)
plt.show()
