#
# TD N°1 - Exercice 3
#

from cmath import pi, exp
import matplotlib.pyplot as plt

def ω(n):
    return exp(2j * pi / n)

# 1. S(n, p)

def S(n, p):
    return sum([
        ω(n) ** (k*p)
        for k in range(n)
    ])

# Illustration
def plot(n):
    p = [p for p in range(0, n+1)]
    Snp = list(map(lambda x : S(n, x), p))
    x = list(map(lambda x : x.real, Snp))
    y = list(map(lambda x : x.imag + n, Snp))
    plt.plot(x, y, 'o-', label="n = " + str(n))

for n in range(1, 9):
    plot(n)

plt.show()
