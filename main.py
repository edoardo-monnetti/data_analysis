# Read data from txt file and plot them √
# Fit gaussian
# Plot the result

import os
import numpy as np
import matplotlib.pyplot as plt
import comma_to_point as ctp

print(os.listdir(os.getcwd()))
for files in (os.listdir(os.getcwd())):

    if ".txt" in files:

        comma_file = ctp.comma_to_point(files)
        data = np.loadtxt(comma_file, skiprows=1)

        x_axis = []
        y_axis = []

        for x_value, y_value in data:
            x_axis.append(x_value)
            y_axis.append(y_value)

        plt.plot(x_axis, y_axis)
        plt.ylabel("Strom")
        plt.xlabel("Mass")
        plt.show()
