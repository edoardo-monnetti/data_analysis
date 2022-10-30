# Read data from txt file and plot them √
# Fit gaussian
# Plot the result

import os
import numpy as np
import matplotlib.pyplot as plt
import comma_to_point as ctp
from scipy.optimize import curve_fit

def gauss(x, y0, A, x0, sigma):
    return y0 + A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
    pass


print(os.listdir(os.getcwd()))

interval_l = input('Select the x-interval you want to plot: \nFrom\n' )
print(' to ')
interval_r = input()


for files in (os.listdir(os.getcwd())):

    if ".txt" in files:

        comma_file = ctp.comma_to_point(files)
        data = np.loadtxt(comma_file, skiprows=1)

        x_axis = []
        y_axis = []

        for x_value, y_value in data:
            if float(interval_l) <= x_value <= float(interval_r):
                x_axis.append(x_value)
                y_axis.append(y_value)

        x_axis = np.asarray(x_axis)
        y_axis = np.asfarray(y_axis)

        mean = 0
        sigma = 0

        n = len(x_axis)
        mean = sum(x_axis * y_axis) / sum(y_axis)
        sigma = np.sqrt(sum(y_axis * (x_axis - mean)**2) / sum(y_axis))

        print(n, mean, sigma)
        
        popt, pcov = curve_fit(gauss, x_axis, y_axis, p0=[0, 1, mean, sigma])

        fitted = gauss(x_axis, *popt)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x_axis, y_axis, c='k', label='Data')
        ax.plot(x_axis, fitted, c='r', label='Best fit')
        ax.legend()

        plt.ylabel("Strom")
        plt.xlabel("Mass")
        plt.show()