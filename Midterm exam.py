import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Data
x = np.array([-5, -3, -4, -1, 1, 3, 5, 7])
y = np.array([2, -1, -4, 1, -2, 1, -3, -2])

# Calculate Pearson correlation
correlation, p_val = pearsonr(x, y)
print(f"Pearson correlation coefficient (r): {correlation}")
print(f"P-value: {p_val}")

# Create scatter plot
plt.figure(figsize=(8,6))
plt.scatter(x, y, c="skyblue", edgecolors="black", s=100)
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)

plt.title("Scatter Plot with Pearson Correlation")
plt.xlabel("X მონაცემები")
plt.ylabel("Y მონაცემები")

# Fit linear trend line
coefficients = np.polyfit(x, y, 1)
trendline = np.poly1d(coefficients)
plt.plot(x, trendline(x), color="red", linewidth=2)

plt.show()
