
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
    
p = Pile()
for i in range(1, 11):
    p.push(i)
while not p.empty():
    print(p.pop(), end="-")
print()

class File:

    def __init__(self, n):
        self.lst = [None] * n
        self.size = n
        self.t = 0
        self.q = 0
    
    def empty(self):
        return self.t == self.q

    def full(self):
        return (self.q + 1) % self.size == self.t

    def add(self, x):
        if self.full():
            raise ValueError("File pleine")
        self.lst[self.q] = x
        self.q = (self.q + 1) % self.size

    def take(self):
        if self.empty():
            raise ValueError("File vide")
        x = self.lst[self.t]
        self.t = (self.t + 1) % self.size
        return x

f = File(20)
for i in range(1, 11):
    f.add(i)
while not f.empty():
    print(f.take(), end="-")
print()
    
