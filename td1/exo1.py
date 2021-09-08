#
# TD N°1 - Exercice 1
#

# 1.a Ecrire la fonction `S(f, N)`

def u(n, f):
    return 1/n + f(n+1) + f(n-1)

def S(f, N):
    return 1 + f(2) + sum([
        ((-1) ** n) * u(2*n + 1, f)
        for n in range(1, N+1)
    ])

# 1.b. Representer les termes avec les différentes fonctions

import matplotlib.pyplot as plt
from math import pi, exp, cos, log

def plot(f):
    x = [x for x in range(1, 101)]
    y = list(map(lambda n : pi / S(f, 10*n), x))
    plt.plot(x, y)

plot(lambda x : exp(-x))
plot(lambda x : cos(x) / x)
plot(lambda x : log(1 + x ** 2) / 1 + x ** 2)

plt.grid()
plt.show()
