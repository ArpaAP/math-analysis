from math import e
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

delta_x = 1e-9

def diff(f, x, method='central'):
    if method == 'central':
        result = (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)
    elif method == 'forward':
        result = (f(x + delta_x) - f(x)) / delta_x
    elif method == 'backward':
        result = (f(x) - f(x - delta_x)) / delta_x
    else:
        raise ValueError("Method must be either 'central', 'forward', or 'backward'")
    return result


f = lambda x: e ** np.sin(0.1*x**2 - 3*x + 4)

result = diff(f, -1)

print(result)

x = np.linspace(-5, 5, 1000)
y = f(x)
yprime = diff(f, x)

ax.set_aspect('equal', adjustable='box')

plt.grid(linewidth=0.5)
plt.xticks(np.arange(-10, 10, 1))
plt.yticks(np.arange(-10, 10, 1))
plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.plot(x, yprime)
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)

plt.show()


