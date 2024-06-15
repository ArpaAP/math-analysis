import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

L=1
x=2

epsilon = 2.5
delta = 1

fig = plt.figure()
ax = fig.add_subplot(111)

def f(x):
    if x >= 2:
        return 2 * x - 5
    else:
        return -x + 3
    

x1 = np.linspace(-5, 2, 1000, endpoint=False)
x2 = np.linspace(2, 5, 1000)


ax.set_aspect('equal', adjustable='box')

plt.grid(linewidth=0.5)
plt.xticks(np.arange(-10, 10, 1))
plt.yticks(np.arange(-10, 10, 1))
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)

plt.plot(x1, [f(i) for i in x1], color='black', linewidth=0.8)
plt.plot(x2, [f(i) for i in x2], color='black', linewidth=0.8)


ax.add_patch(
    patches.Rectangle(
        (-10, L - epsilon),
        20, 2 * epsilon,
        edgecolor = 'blue',
        facecolor = 'skyblue',
        alpha=0.5,
        fill=True,
   ))

ax.add_patch(
    patches.Rectangle(
        (x - delta, -10),
        2 * delta, 20,
        edgecolor = 'red',
        facecolor = 'lightpink',
        alpha=0.5,
        fill=True,
   ))

plt.show()