import numpy as np
import math

# Estimation project: Bottle Water Volume Estimator

class Bottle:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
    
    # Method to calculate volume of the bottle in liters
    def calculate_volume(self):
        radius = self.diameter / 2
        volume_cm3 = math.pi * (radius**2) * self.height
        return volume_cm3 / 1000  # Convert cm^3 to liters

# Function to calculate statistics (average, standard deviation, and relative error)
def calculate_stats(volumes):
    avg_volume = np.mean(volumes)
    std_dev = np.std(volumes)
    relative_error = (std_dev / avg_volume) * 100  # Relative error as a percentage
    return avg_volume, std_dev, relative_error

# List of bottles with varying diameters and heights
bottles = [
    Bottle(6.5, 20),  # in cm
    Bottle(6.3, 22),
    Bottle(6.1, 21),
    Bottle(6.2, 21),
    Bottle(6.4, 22),
    Bottle(6.0, 20),
    Bottle(6.3, 21),
    Bottle(6.2, 20),
    Bottle(6.1, 21),
    Bottle(7.0, 25)
]

# Calculate volumes for each bottle
volumes = [b.calculate_volume() for b in bottles]

# Calculate statistics
average_volume, absolute_error, relative_error = calculate_stats(volumes)

# Output the results
print(f"Average Volume: {average_volume:.4f} liters")
print(f"Absolute Error (Standard Deviation): {absolute_error:.4f} liters")
print(f"Relative Error: {relative_error:.2f}%")

# Display individual volumes
print(f"Individual Volumes: {volumes}")

# Plot the data using matplotlib
import matplotlib.pyplot as plt

plt.bar(range(1, len(volumes)+1), volumes)
plt.xlabel('Bottle Number')
plt.ylabel('Volume (liters)')
plt.title('Volume of Water Each Bottle Can Hold')
plt.show()