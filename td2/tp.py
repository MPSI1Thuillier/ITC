# Définition des classes nécessaires

class Cell:
    
    def __init__(self, x):
        self.val = x
        self.next = None

class Pile:

    def __init__(self):
        self.lst = None

    def empty(self):
        return self.lst is None

    def push(self, x):
        c = Cell(x)
        c.next = self.lst
        self.lst = c

    def pop(self):
        if self.empty():
            raise ValueError("Pile vide")
        c = self.lst
        self.lst = c.next
        return c.val

    def peek(self):
        if self.empty():
            raise ValueError("Pile vide")
        return self.lst.val

# Question 1

def triPile(a):
    # Défini le résultat et la pile à utiliser
    res = []
    pile = Pile()

    # On parcourt les éléments à trier
    for e in a:
        # Tant que la pile est non vide et que l'élément à ajouter est plus grand
        # Autrement dit, qu'il ne va pas casser le sens croissant de la pile
        while not pile.empty() and e > pile.peek():
            # On le récupère pour l'ajouter
            toAdd = pile.pop()

            # On vérifie qu'il est bien plus grand que le dernier élément du résultat
            if len(res) == 0 or (len(res) > 0 and res[len(res) - 1] < toAdd):
                res.append(toAdd)
            else:
                # Autrement, c'est que le tri n'est pas faisable
                return False
        
        # Dans tous les cas, on ajoute l'élément dans la pile
        pile.push(e)

    # On termine par vider la pile
    while not pile.empty():
        # On le récupère pour l'ajouter
        toAdd = pile.pop()

        # On vérifie qu'il est bien plus grand que le dernier élément du résultat
        if len(res) == 0 or (len(res) > 0 and res[len(res) - 1] < toAdd):
            res.append(toAdd)
        else:
            # Autrement, c'est que le tri n'est pas faisable
            return False
    
    # Si le tri s'est effectué, on ressort le résultat
    return res

# Test de la fonction avec les exemples du la question 1.a)
print(triPile([2, 4, 1, 3]))
print(triPile([3, 1, 2, 5, 4]))
print(triPile([4, 5, 3, 7, 2, 6]))
