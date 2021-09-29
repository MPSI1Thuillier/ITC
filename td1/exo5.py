#
# TD N°1 - Exercice 5
#

from math import log
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

# pour x > -1/n et n ≥ 1
def f(n, x):
    return x - n * log(x + 1/n)

# y = 0
plt.plot([-3, 12], [0, 0])

# Graph de f_n(x) pour 1 ≤ n ≤ 10
xn = []
def plot(n):
    x = np.arange(-1/n + 0.1, 10, 0.01)
    y = list(map(lambda x : f(n, x), x))
    plt.plot(x, y)
    #fsolve(f) # to get done

for n in range(1, 11):
    plot(n)

plt.show()
