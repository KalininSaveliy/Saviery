from matplotlib import pyplot as plt
import numpy as np


x = np.linspace(-10, 10, 100, endpoint=False)
q = np.arange(-9, 9, 1)

fig, ax = plt.subplots(figsize=(10, 5))
for k in q:
    if k != 0:
        y_tau = 1/2 * ((x/k)**2 - k**2)
        plt.plot(x, y_tau, color="blue", label="k")
        y_sigma = 1/2 * (k**2 - (x/k)**2)
        plt.plot(x, y_sigma, color="red")

plt.show()
