import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def gauss(x, y0, A, x0, sigma):
    return y0 + A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
    pass

x = np.linspace(0, 10, 100)
y = gauss(x, 0, 1, 5, 2)

#adding noise
yn = y + 0.2 * np.random.normal(size=len(x))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, c='k', label='Function')
ax.scatter(x, yn)

par_opt = np.zeros(4)
print(par_opt)

n = len(x)
mean = sum(x*y)/n
sigma = sum(y*(x-mean)**2)/n

par_opt, cov_opt = curve_fit(gauss, x, yn, p0=[0, 1, mean, sigma])

print(par_opt)

fitted = gauss(x, *par_opt)
ax.plot(x, fitted, c='r', label='Best fit')
ax.legend()

plt.show()

