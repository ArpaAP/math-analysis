import matplotlib.pyplot as plt
import venn

A = {1, 2, 3, 4, 5}
B = {3, 5, 7}
C = {2, 4, 6, 8}

venn.venn({'A': A, 'B': B, 'C': C}, cmap="plasma")

plt.show()