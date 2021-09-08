#
# TD N°1 - Exercice 2
#

# On wrap la logique de la matrice dans un object pour la manipuler

class Matrice:

    # Initialisation avec les données (un tableau en deux dimension)
    def __init__(self, data):
        self.data = data

    # Affichage de la matrice
    def afficher(self):
        for i in range(0, len(self.data)):
            print("| ", end="")
            for j in range(0, len(self.data[i])):
                print(self.data[i][j], end="\t")
            print(" |", end="\n")
        print("")
    
    # Somme avec une autre matrice
    def __add__(self, other):
        assert(len(self.data) == len(other.data))
        return Matrice([
            [
                self.data[i][j] + other.data[i][j]
                for j in range(0, len(self.data[i]))
            ]
            for i in range(0, len(self.data))
        ])

    # Somme avec une autre matrice
    def __sub__(self, other):
        assert(len(self.data) == len(other.data))
        return Matrice([
            [
                self.data[i][j] - other.data[i][j]
                for j in range(0, len(self.data[i]))
            ]
            for i in range(0, len(self.data))
        ])

    # Support pour la fonction `sum()`
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
    
    # Produit avec une autre matrice
    def __mul__(self, other):
        return Matrice([
            [
                sum([
                    self.data[i][k] * other.data[k][j]
                    for k in range(0, len(self.data[i]))
                ])
                for j in range(0, len(self.data[i]))
            ]
            for i in range(0, len(self.data))
        ])

    # Elevation à une puissance
    def __pow__(self, other):
        result = self
        if other == 0:
            return Matrice([[1 if i == j else 0 for j in range(len(self.data))] for i in range(len(self.data))])
        while other > 0:
            if other & 1 == 1:
                result = result * self
            result = result * result
            other = other >> 1
        return result
    
    # Transposée de la matrice
    def transposee(self):
        return Matrice([
            [
                self.data[j][i]
                for j in range(0, len(self.data[i]))
            ]
            for i in range(0, len(self.data))
        ])

# Application pour 2 <= n <= 7

for n in range(2, 8):
    I = Matrice([
        [
            1 if i == j else 0
            for j in range(1, n+1)
        ]
        for i in range(1, n+1)
    ])
    A = Matrice([
        [
            2 if i == j and j < n else
            1 if i == j and j == n else
            -1 if abs(i - j) == 1 else
            0
            for j in range(1, n+1)
        ]
        for i in range(1, n+1)
    ])
    T = Matrice([
        [
            1 if i >= j else 0
            for j in range(1, n+1)
        ]
        for i in range(1, n+1)
    ])
    N = Matrice([
        [
            1 if i == j + 1 else 0
            for j in range(1, n+1)
        ]
        for i in range(1, n+1)
    ])

    # 1. Afficher les matrices
    print("n = " + str(n))
    A.afficher()
    T.afficher()
    N.afficher()

    # 2. Calculer la somme

    somme = sum([
        N ** k
        for k in range(0, n)
    ])
    somme.afficher()

    # 3. Calculer T*(I-N)

    q3 = T * (I - N)
    q3.afficher()

    # 4. Calculer A * T * t(T)

    q4 = A * T * T.transposee()
    q4.afficher()
